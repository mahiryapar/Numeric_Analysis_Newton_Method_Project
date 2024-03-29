import math
from sympy import symbols,sympify, diff

x = symbols("x")
y = symbols("y")

def bilgi_al():
    while True:
        fx = input("Newton Metodunu uygulamak istediğiniz fonksiyonu giriniz -> ")
        try:
            fx = sympify(fx, locals={"pi": math.pi, "oo": math.inf, "e": math.e})
        except:
            print("Fonksiyon girdisinde hata! Lütfen tekrar deneyiniz.")
            continue
        break
    while True:
        try:
            error_level = float(input("Hata seviyesi giriniz (Örneğin:0.001)->"))
        except ValueError:
            print("Lütfen gecerli bir değer giriniz!")
            continue
        break
    while True:
        try:
            p0 = float(input("P0 değerini giriniz ->"))
        except ValueError:
            print("Lütfen gecerli aralık değerleri giriniz!")
            continue
        break
    return fx ,error_level, p0


def newton_method(fx, error_level, p_0):
    current_iter = 0
    max_iter =100
    fxt = diff(fx, x)
    while current_iter < max_iter :
        current_iter +=1
        derivative_value = fxt.subs(x,p_0)
        if derivative_value == 0:
            print("Türev sıfıra yakınsadı. Kök bulunamadı.")
            return None, 0
        p_n = p_0 - (fx.subs(x, p_0) / derivative_value)
        if abs(p_n-p_0) < error_level:
            return p_n, current_iter
        p_0 = p_n


def main():
    fx, error_level, p0= bilgi_al()
    root, current_iter = newton_method(fx, error_level, p0)
    if root:
        print(f"Girilen Bilgilere Göre Bulunan Kök: {root}")
        print(f"Kök {current_iter}. adımda bulunmuştur.")


if __name__ == "__main__":        #programın çalışmasını sağlıyor
    main()                       #moduler olarak çağrılırsa main çalışmasın

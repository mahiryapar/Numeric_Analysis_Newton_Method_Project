import math
from sympy import symbols,sympify, diff,E,oo,pi

x = symbols("x")
y = symbols("y")


def turev(fx):
    fxt = diff(fx, x)
    return fxt

def bilgi_al():
    while True:
        fx = input("Newton Metodunu uygulamak istediğiniz fonksiyonu giriniz -> ")
        try:
            fx = sympify(fx, locals={"pi": pi, "oo": oo, "e": E})
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
    while(current_iter < max_iter):
        current_iter +=1
        derivative_value = diff(fx, p_0)
        if(derivative_value == 0):
            print("Türev sıfıra yakınsadı. Kök bulunamadı.")
            break
        p_n = p_0 - (fx.subs(x, p_0) / derivative_value)
        if(abs(p_n-p_0) < error_level):
            return p_n
        p_0 = p_n


def main():
    fx, error_level, p0= bilgi_al()
    print(f"Error level :{error_level}, p0 değeri:{p0}")
    print(turev(fx))
    root = newton_method(fx, error_level, p0)
    print(root)


if __name__ == "__main__":        #programın çalışmasını sağlıyor
    main()                       #moduler olarak çağrılırsa main çalışmasın

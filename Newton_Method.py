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
            p_0 = float(input("Başlangıç değer giriniz ->"))
        except ValueError:
            print("Lütfen gecerli bir değer giriniz!")
            continue
        break
    return fx ,error_level, p_0


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
        if(p_n < error_level):
            return p_n
        p_0 = p_n

    if current_iter < max_iter:
        print(f"Kök bulundu: {p_n} (iterasyon sayısı: {current_iter})")
    else:
        print("Maksimum iterasyon sayısına ulaşıldı. Kök bulunamadı.")

def main():
    fx, error_level, p_0 = bilgi_al()
    print(f"Error level :{error_level}")
    print(turev(fx))
    root = newton_method(fx, error_level, p_0)

if __name__ == "__main__":        #programın çalışmasını sağlıyor
    main()                       #moduler olarak çağrılırsa main çalışmasın

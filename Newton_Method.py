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
            print("Kök bulmak istediğiniz bir aralık belirleyiniz.")
            range_start_value = float(input("Aralığın başlangıç değerini giriniz ->"))
            range_finish_value = float(input("Aralığın bitiş değerini giriniz ->"))
        except ValueError:
            print("Lütfen gecerli aralık değerleri giriniz!")
            continue
        break
    return fx ,error_level, range_start_value, range_finish_value


def newton_method(fx, error_level, range_start_value, range_finish_value):
    p_0 = float(range_start_value+range_finish_value)/2 # p0 baslangic değerimiz.
    current_iter = 0
    max_iter =100
    while(current_iter < max_iter):
        current_iter +=1
        p_n = p_0 -fx.subs(x, p_0) / diff(fx, x)
        if(p_n < error_level):
            return p_n
        p_0 = p_n

    if current_iter < max_iter:
        print(f"Kök bulundu: {p_n} (iterasyon sayısı: {current_iter})")
    else:
        print("Maksimum iterasyon sayısına ulaşıldı. Kök bulunamadı.")

def main():
    fx, error_level, range_start_value, range_finish_value = bilgi_al()
    print(f"Error level :{error_level}, Aralık başlangıcı :{range_start_value}, Aralık bitişi :{range_finish_value}")
    print(turev(fx))
    root = newton_method(fx, error_level, range_start_value, range_finish_value)


if __name__ == "__main__":        #programın çalışmasını sağlıyor
    main()                       #moduler olarak çağrılırsa main çalışmasın

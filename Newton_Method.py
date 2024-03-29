import math
from sympy import symbols,sympify, diff

x = symbols("x")
y = symbols("y")
e = symbols("e")
pi = math.pi
inf = math.inf

def turev(fx):
    fxt = diff(fx, x)
    return fxt

def bilgi_al():
    while True:
        fx = input("Newton Metodunu uygulamak istediğiniz fonksiyonu giriniz -> ")
        try:
            fx = sympify(fx)
        except:
            print("Fonksiyon girdisinde hata! Lütfen tekrar deneyiniz.")
            ctrl = True
            continue

        while True:
            try:
                error_level = float(input("Hata seviyesi giriniz (Örneğin:0.001)->"))
                break
            except ValueError:
                print("Lütfen gecerli bir değer giriniz!")
                continue
        while True:
            try:
                print("Kök bulmak istediğiniz bir aralık belirleyiniz.")
                range_start_value = float(input("Aralığın başlangıç değerini giriniz ->"))
                range_finish_value = float(input("Aralığın bitiş değerini giriniz ->"))
                break
            except ValueError:
                print("Lütfen gecerli aralık değerleri giriniz!")
                continue

    return fx ,error_level, range_start_value, range_finish_value



def print_yaz():
    fx, error_level, range_start_value, range_finish_value = bilgi_al()
    print(f"Error level :{error_level}, Aralık başlangıcı :{range_start_value}, Aralık bitişi :{range_finish_value}")
    print(turev(fx))

print_yaz()

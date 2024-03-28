import math
from sympy import symbols,sympify, diff

x = symbols("x")
y = symbols("y")
e = symbols("e")
pi = math.pi
inf = math.inf

def turev(fx):
    fxt = diff(fx,x)
    return fxt

def bilgi_al():
    ctrl = True
    while ctrl == True:
        ctrl = False
        fx = input("Newton Metodunu uygulamak istediğiniz fonksiyonu giriniz -> ")
        try:
            fx = sympify(fx)
        except:
            print("Fonksiyon girdisinde hata! Lütfen tekrar deneyiniz.")
            ctrl = True
            continue
        ctrl = False
        return fx


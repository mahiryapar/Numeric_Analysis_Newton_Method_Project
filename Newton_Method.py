import math
from sympy import symbols, diff

x = symbols("x")
y = symbols("y")
e = math.e
pi = math.pi
inf = math.inf

fx = x**2 + 3*x + 2


def turev(fx):
    fxt = diff(fx,x)
    return fxt
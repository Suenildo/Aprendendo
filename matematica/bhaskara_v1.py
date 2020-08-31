"""
Cálculo das raízes de uma equação do 2º utilizando
o sympy
"""

from sympy import *


def equacao_2grau():
    x = Symbol('x')
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    raizes = solve(a * (x ** 2) + b * x + c, x)
    print(f' As raízes da equação são: {raizes}')


equacao_2grau()

# o valor int, pode ser substituído por float.

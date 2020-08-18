"""
Cálculo das raízes de uma equação do 2º utilizando
a fórmula de Bhaskara
"""
from math import sqrt

print('Toda equação do 2ª grau, é da forma:')
print('=*=' * 7)
print('(a)X² + (b)X + c = 0')
print('=*=' * 7)
print()
print('Portanto, para resolver a sua equação, entre com os coeficientes: a, b e c')
print()


def calculo_das_raizes(a, b, c):
    raizes = []
    delta = b ** 2 - (4 * a * c)

    if (delta > 0):
        r1 = (-b + sqrt(delta)) / (2 * a)
        r2 = (-b - sqrt(delta)) / (2 * a)
        raizes.append(r1)
        raizes.append(r2)
    elif (delta == 0):
        r = -b / (2 * a)
        raizes.append(r)
    else:
        r1 = complex(-b / (2 * a), sqrt(abs(delta)) / (2 * a))
        r2 = complex(-b / (2 * a), - sqrt(abs(delta)) / (2 * a))
        raizes.append(r1)
        raizes.append(r2)

    return raizes


outra_equacao = 's'

while outra_equacao in 'sS':
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    raizes = calculo_das_raizes(a, b, c)

    if (len(raizes) == 1):
        print('X =', raizes[0])
    else:
        print('X1 =', raizes[0])
        print('X2 =', raizes[1])

    outra_equacao = input('\nQuer resolver outra equação: S ou N: ')
    print()
    print('Bhaskara Akaria, também conhecido como Bhaskaracharya, '
          'nasceu na cidade de Vijayapura, na Índia, em 1114, e viveu até de 1185.')

"""
Algumas funções simples da matemática para exemplificar
a utilização de funções.
"""

def soma(a, b):
    print(f'O resultado da soma entre {a} e {b} é  {a + b} ')


def subtrair(a, b):
    print(f'O resultado da  subtração entre {a} e {b} é {a - b}')


def divide(a, b):
    print(f'O resultado da divisão entre {a} e {b} é {a / b}')


def multiplicar(a, b):
    print(f'O resultado da multiplicação entre {a} e {b} é {a * b}')


try:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o primeiro número: '))

    soma(a, b)
    subtrair(a, b)
    multiplicar(a, b)
    divide(a, b)


except ValueError:
    print('Operação inválida')
except ZeroDivisionError:
    print('Operação não permitida')
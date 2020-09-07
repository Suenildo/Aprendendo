"""
Esse programa verifica se um número é primo.
"""

import math


def numPrimo(num):
    """
    Verificando se um número
    é primo.
    """
    if (num % 2) == 0 and num > 2:
        return print("Este número não é primo!!!")
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return print("Este número não é primo")
    return print("Este número é primo")


numPrimo(int(input('Digite um núemro para saber se é primo: ')))

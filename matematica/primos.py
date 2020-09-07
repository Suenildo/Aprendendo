"""
Esse programa verifica se um número é primo,
Somente para números Naturais.
"""

import math


def numPrimo(num):
    """
    Verificando se um número2
    é primo.
    """
    if [(num % 2) == 0 and num > 2] and num < 2:
        return print("Este número não é primo!!!")
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return print("Este número não é primo")
    return print("Este número é primo")


numPrimo(int(input('Digite um núemro para saber se é primo: ')))

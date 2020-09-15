"""
Dado um número inteiro , inverta sues dígitos.
Examplos:
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
"""


def inverte_inteiro(num):
    """
    :param num: Número inteiro
    :return: Número inteiro invertido
    """
    auxiliar = str(num)
    mad = auxiliar[::-1]
    saida = int(mad)
    return saida


num = 123

print(inverte_inteiro(num))



'''a = 'silvio'
b = a[::-1]
print(b)'''

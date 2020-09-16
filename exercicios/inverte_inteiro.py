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
'''

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

'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = 0
    if x > 0:
        flag = 1
    else:
        flag = -1
    x = str(abs(x))
    s = int(x[::-1])
    if s <= 2 ** 31 - 1:
        return flag * s
    else:
        return 0


x = int(input("Digite o número a ser invertido:"))

invertido = reverse(x)


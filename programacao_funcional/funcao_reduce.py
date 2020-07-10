"""
O que essa função faz:
serve pra (reduzir) um iterável (como uma lista) a um único valor.
"""
from functools import reduce


def somar(x, y):
    return x + y


lista = [0, 6, 12, 42, 51]

soma = reduce(somar, lista)

print(f'O valor da soma dos itens da lista é: {soma}')

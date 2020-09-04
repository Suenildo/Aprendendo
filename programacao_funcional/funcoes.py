"""
Função com vários argumentos definidos de forma
genérica com (*args)
O (*args) devolve uma tupla contendo os argumentos.

Os exemplos vão levar em consideração somente números.
"""


def multiplica(*args):
    if args == 0:
        return 0
    produto = 1
    for fator in args:
        produto = produto * fator
    return produto


print(multiplica(0))
print(multiplica(2, 3))
print(multiplica(2, 3, 5))
print(multiplica(2, 3, 5, 7))

print()
print('=*=' * 10)

# Podemos notar que eu posso passar quantos argumentos eu quiser.

'''Como o (*args) retorna, no seu tipo, uma tupla com os valores,
se nós fizermos uma função soma, ficaria assim:'''

def soma(*args):
    return sum(args)



print(soma(1, 5, 9, 11))
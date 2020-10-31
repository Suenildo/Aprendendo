"""
Geradores são eficazes e eficientes, principalmente pela
economia de memória.

Com geradores podemos criar um objeto iterável sem ter de
construí-lo dentro de uma classe.

Todo gerador é um iterável, a recíproca não é verdadeira.

Geradores podem ser criados com funções geradoras.
Geradores podem ser criados com expressões geradoras.


Diferença entre return e yield:
return : após o return, a função é encerrada e a execução sai da função.
yield : A função não é encerrada, fica aguardando o próximo next.
"""


def numero_crescente(numero_grande):
    for numero in range(numero_grande + 1):
        yield numero


meu_gerador = numero_crescente(5)
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
# print(next(meu_gerador))  Aqui teremos o erro: StopIteration

print()

# Imprimindo todos em uma lista:

meu_gerador = list(numero_crescente(6))
print(meu_gerador)

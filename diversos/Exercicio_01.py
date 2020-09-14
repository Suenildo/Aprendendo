"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

def twosum(entrada, saida):
    """
    :param entrada: lista de inteiros
    :param saida: numero inteiro
    :return: os índices dos numero usados na soma em forma de lista
    """
    for i in range(len(entrada)):
        auxiliar = saida - entrada[i]
        for j in range(i + 1, len(entrada)):
            if entrada[j] == auxiliar:
                return [i, j]


entrada = [2, 5, 8, 7, 9]
saida = 12
resposta = twosum(entrada, saida)
print(f'Os números que satisfazem a condição são os de índices: {resposta}')
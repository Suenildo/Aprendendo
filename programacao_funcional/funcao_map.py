"""
O que essa função faz:
Tem como objetivo aplicar uma função a todos os elementos
de uma sequência, retornando uma nova sequência com o resultado.
"""
valor = [1, 2, 3, 4, 5]

def dobro(x):
    return x * 2

valor_dobro = map(dobro, valor)

valor_dobro = list(valor_dobro)  # Inserindo o objeto em uma linha

print(valor_dobro)




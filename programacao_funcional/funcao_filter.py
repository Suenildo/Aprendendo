"""
O que essa função faz:
A função Filter pega uma lista e aplica uma regra, onde
compara cada elemento da lista contra a regra de filtragem booleana.
Uma vez aplicada a condição, retorna um subconjunto da lista original
"""

lista = [2, 5, 10, 51, 95, 102]

# Vamos criar uma função que somente retorna valores pares:

def pares(i):
    if i % 2 == 0:
        return i
print('Usando a função "filter" para retornar os valores pares:')
print()
lista_pares = filter(pares, lista)

print(list(lista_pares))

"""
O que essa função faz:
Esta função retorna uma lista de tuplas, onde a i-ésima tupla contém
o i-ésimo elemento de cada um dos argumentos.
"""

lista_nome = ['aba', 'bola', 'cola', 'dado', 'elo']
lista_numero = [1, 2, 3, 4, 5]
lista3 = ['livro', 'jogador', 'aluno', 'jogo', 'corrente']

for numero, nome in zip(lista_numero, lista_nome):
    print(numero, nome)

for numero, nome, dono in zip(lista_numero, lista_nome, lista3):
    print(numero, nome, dono)
print()
# Quando as sequências possuem tamanhos diferentes

list1 = ['caju', 'goiaba', 'banana']
list2 = ['cajuada', 'goiabada']
lista = list(zip(list1, list2))
# Repara que o retorno é com o número de elementos da menor lista.
print(lista)

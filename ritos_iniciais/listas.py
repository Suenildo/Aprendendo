"""
Uma lista é uma estrutura de dados composta por itens organizados
de forma linear, na qual cada um pode ser acessado a partir de um
índice, que representa sua posição na coleção (iniciando em zero).

https://www.devmedia.com.br
"""
# Criação de uma lista:

lista01 = ['abacaxi', 'banana', 'coco', 'damasco', 'uva']
lista02 = list()
lista03 = list([1, 2, 3])
print(lista01)
print(lista02, 'Essa lista está vazia')
print(lista03)

'''
A lista é indexada de seguinte forma:
Tomemos como exemplo a lista01:
+-------------+-------------+-------------+-------------+-------------+
| "abaxaxi"   |  "banana"   |   "coco"    |  "damasco"  |    "uva"    |
+-------------+-------------+-------------+-------------+-------------+
      0              1             2              3            4
'''

# preenchendo uma lista com o for:
for item in range(0, 12):
    lista02.append(item)
print(lista02)


# Podemos percorre uma lista:
print()
for itens in lista01:
    print(itens)


# Podemos verificar os índices de uma lista:
print()
for indice, item in enumerate(lista01):
    print(indice, item)
print()


# Inserindo itens em uma lista:
lista01.append('goiaba')
print(lista01)

lista03.insert(0, 'a')  # posso inserir na posição desejada
print(lista03)


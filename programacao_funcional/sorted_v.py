"""
sorted:
A função 'sorted' é utilizada  caso você queira criar uma
nova lista com os valores da primeira, mantendo esta
com os valores originais. Caso a intensão seja somente
ordenar a lista original, utilize a  função 'sort'.
"""

# Exemplos:
lista_1 = [0, 1, 2, 5, 8, 100, 3]
lista_1.sort()
print(lista_1)  # A lista foi modificada, criada outra lista

print()

lista_2 = [0, 1, 2, 5, 8, 100, 3]
print(sorted(lista_2))
print(lista_2)  # A lista não foi modificada.

print()

# Vamos ordenar uma lista de dicionários
animais = [
    {"felino": "gato", "idade": "cinco anos"},
    {"felino": "leão", "idade": "sete anos"},
    {"felino": "tigre", "idade": "seis anos"},
    {"felino": "guepardo", "idade": "quatro anos"}
]
print(animais)

print(sorted(animais, key=lambda tipo: tipo["felino"]))

print()

notas = [
    {"Matéria": "Matemática", "nota": 7},
    {"Matéria": "Português", "nota": 8},
    {"Matéria": "Química", "nota": 9},
    {"Matéria": "Física", "nota": 5},
    {"Matéria": "Inglês", "nota": 10},
]

print('Notas da maior para a menor:')
print(sorted(notas, key=lambda nota: nota["nota"], reverse=True))

print()

print('Notas da menor para a maior:')
print(sorted(notas, key=lambda nota: nota["nota"]))


"""
List Comprehension é uma construção sintática disponível
em algumas linguagens de programação para criação de uma lista
baseada em listas existentes. Ela segue a forma da notação de
definição de conjunto matemática como forma distinta para uso de
funções de mapa e filtro.
Foi concebida na PEP 202 e é uma forma concisa de criar e manipular listas.
"""

import math

# Forma simples de criação de uma lista:
z = [x for x in range(6)]
print(z)
print()


# Criando uma lista com um for:
print('Com o for:')
q = []
for a in range(0, 10):
    if math.sqrt(a) % 1 == 0:
        q.append(a)

print(q)
print()

# Criando a mesma lista com list comprehension:
print('Com List Comprehension:  ')
q = [a for a in range(0, 10) if math.sqrt(a) % 1 == 0]

print(q)

'''
Mesmo dando mais praticidade ao código, as "list comprehensions",
devem ser usadas com moderação, pois torna o código mais complexo
para que está lendo.
Lempre-se:  "Readability counts".
'''


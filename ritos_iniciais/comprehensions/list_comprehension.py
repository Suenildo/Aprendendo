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


# Você pode fazer chamada de funções na comprehension:
def titularizar(palavra):
    palavra = palavra.replace(palavra[0], palavra[0].upper())
    return palavra


''' Nessa função, se a palavra tiver outra letra igual 
a do índice "0", ela a colocará como maiúscula também.
Cuidado com esse tipo de erro.'''

paises = ['brasil', 'espanha', 'bolívia', 'paraguai']
corrigido = [titularizar(paises) for paises in paises]

print(corrigido)

print()
print('*=*' * 15)

print("Uma cusiosidade:")
''' Em python:
 - 0 é sempre falso por padrão; e
 - 1 é sempre verdadeiro por padrão.
Então se você faz uma operação que tem como retorno 0, o python,
por padrão vai considerá-la falsa, veja um exemplo clássico:'''

valores = [1, 2, 3, 4, 5, 6, 7, 8]

numero = [valor for valor in valores if valor % 2]
print(numero)

''' Você achou que ele retornaria os valores páres, mas não,
ele retornou os ímares, por que:
Isso aconteceu porque como o módulo de um númeo par por 2
dá resultado 0, o pyhon o clasificou como False, para retornar
os pares, faremos uma modificação na "comprehencion".'''

numero_pares = [valor for valor in valores if not valor % 2]
print(numero_pares)

'''
Mesmo dando mais praticidade ao código, as "list comprehensions",
devem ser usadas com moderação, pois torna o código mais complexo
para que está lendo.
Lempre-se:  "Readability counts".
'''
print()

print('=*=' * 15)

# Usando uma comprehension com zip
print('Comprehension com a função ZIP')
x = [1, 3, 6]
y = [6, 4, 2]

d2 = [a * b for a, b in zip(x, y)]
print(d2)
resultado = sum(d2)
print(resultado)
d1 = list(zip(x, y))
print(d1)

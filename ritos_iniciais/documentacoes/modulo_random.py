"""
Este módulo implementa geradores de números pseudoaleatórios
para várias distribuições.
"""

import random

print('Printa números aleatórios em um intervalo de 0 a 1')
for j in range(5):
    print(random.random())

print()
print('Printa números aleatórios em um intervalo desejado')

for i in range(10):
    print(random.uniform(3, 6))

print()
print('Printa números inteiros, aleatórios, em um intervalo estabelecido')

for k in range(15):
    print(random.randint(0, 25), end=', ')
print()

print()
print('Printa um valor aleatório entre um iterável')
frutas = ['banana', 'maçã', 'uva']
print(f'A fruta escolhida foi: {random.choice(frutas)}')

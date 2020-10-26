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

print()
print('É uma função que embaralha dados')
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)

'''
Esta não é a maneira ideal de importar um módulo,
pois você aloca muita coisa na memória, o ideal é 
sempre otimizar os importes, desde que, você
saiba previamente quais funções do pacote você
irá utilizar

Caso eu não queira usar a (sintaxe) usada nesse arquivo,
como por exemplo: random.shuffle(numeros)
Onde eu tenho que colocar o nome do módulo mais a 
função.
Eu importria o módulo da seguinte forma:

from random import *

assim a sintaxe ficaria:
shuffle(numeros)

Entretanto, a forma pythonica de realizar vários imports é:

from random import (randint,
                    shuffle,
                    uniform,
                    random
                    )


'''

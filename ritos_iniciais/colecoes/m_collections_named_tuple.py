"""
Esse método retorna uma nova subclasse de tupla chamada typename.
A nova subclasse é usada para criar objetos semelhantes a tuplas
que possuem campos acessíveis por pesquisa de atributo, além de
serem indexáveis e iteráveis.
"""
from collections import namedtuple

# Como podemos declarar:

# Declaração mais comum:
jogador = namedtuple('jogador', ['nome', 'idade', 'time'])
jogador_1 = jogador(nome='Neymar', idade=25, time='Barcelona')

print(jogador_1)

'''
Outros métodos de declaração:
 - jogador = namedtuple('jogador', 'nome, idade, time')
 - jogador = namedtuple('jogador', 'nome idade time')
 '''

print()

# A partir da declaração, podemos acessar os parâmetros
print(jogador_1[0])
print(jogador_1[1])
print(jogador_1[2])
print(f'Jogador: {jogador_1[0]}, idade {jogador_1[1]}, seu time {jogador_1[2]}')

print()

# OU
print(jogador_1.nome)
print(jogador_1.idade)
print(jogador_1.time)
print(f'Jogador: {jogador_1.nome}, idade {jogador_1.idade}, seu time {jogador_1.time}')

print()
nt = namedtuple('type', 'field')
print(dir(nt)[-10:])

'''
['__subclasshook__', '_asdict', '_field_defaults', '_fields', '_fields_defaults', 
'_make', '_replace', 'count', 'field', 'index']

Os métodos com undercore na frente, significam que eles estão ocultos, entretantos
vc pode acessá-los, você pode até não precisar, mas pode fazê-lo.
'''


"""
um iterador é um objeto que contém um número contável de valores.
Um iterador é um objeto que pode ser iterado, o que significa que
você pode percorrer todos os valores.
Tecnicamente, em Python, um iterador é um objeto que implementa o
protocolo do iterador, que consiste nos métodos __iter __ () e __next __ ().

Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.
Eles são contêineres iteráveis dos quais você pode obter um iterador.

Todos esses objetos têm um método iter () que é usado para obter um iterador:
"""

print('Exemplos:')

frutas = ("maçã", "banana", "abacate")
iterando = iter(frutas)

print(next(iterando))
print(next(iterando))
print(next(iterando))


'''Tomar cuidado para não pedir o "next" sem haver, isso gera
o seguinte erro: ((StopIteration))'''

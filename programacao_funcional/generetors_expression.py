"""
O (generetors expression) funciona, praticamente como uma
List comprehension ou set, dictionary comprehension, com a seguinte
diferença:
O Generator expressions é  mais adequado do que ascomprehensions
 citadas, quando queremos somente gerar sequências de elementos para iterar
 sobre, pois geram somente um elemento por  vez, ao contrário das
 comprehensions citadas pois estas geram uma lista inteira em memória.
"""

from sys import getsizeof

# Vamos gerar algumas comprehensions

lista = getsizeof([x ** 2 for x in range(100)])
conjunto = getsizeof({x ** 2 for x in range(100)})
dicionario = getsizeof({x: x ** 2 for x in range(100)})
gerador = getsizeof(x ** 2 for x in range(100))

print('Para a execução gastaremos em memória:')
print(f'list comprehensio: {lista} bytes')
print(f'list comprehensio: {conjunto} bytes')
print(f'list comprehensio: {dicionario} bytes')
print(f'list comprehensio: {gerador} bytes')

'''Exemplos pegos no curso:
Geek University
Evolua seu lado geek! 
Programação em Python do Básico ao avançado, aula 65 Generators
Udemy
*****Recomendo o curso, muito bom e didático!*****

(((foram feitas algumas modificações por mim))) '''

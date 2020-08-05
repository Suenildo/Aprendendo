"""
Counter é uma subclasse dicionário para contar objetos.
É uma coleção em que os elementos são armazenados como
chaves do dicionário e suas contagens são armazenadas como
valores do dicionário. É permitido que contagens sejam
qualquer valor inteiro, incluindo contagens zero ou negativas.
"""

from collections import Counter

print('Retirado da Documentação do Python')
a = Counter()                           # a new, empty counter
b = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
d = Counter(cats=4, dogs=8)             # a new counter from keyword args

print(a)
print(b)
print(c)
print(d)

print()

print('=*=' * 25)

print('Exemplos:')
# Será exibido um dicionário com as repetições de cada caracter inclusive o espaço
frase = 'Aqui serão contadas todas as repeticoes de letras e os espacos'
contador = Counter(frase)
print(contador)

print()

frase1 = '''Aqui serão contadas as repetições das palavras que estão
nesta frase, serão contadas uma por uma'''
palavra = frase1.split()
res = Counter(palavra)
print(res)

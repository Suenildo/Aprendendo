"""
Função max() - Retorna o maior valor contido em um iterável ou entre elementos.
Função min() - Retorna o menor valor contido no iterável, ou entre elementos
"""

# Exemplos de max():

a = [1, 5, 8, 74]
b = (1, 5, 8, 74)
c = {1, 5, 8, 74}
d = {'am': 1, 'dois': 5, 'três': 8, 'quatro': 74}

print(f'Eu sou o maior valor de a: {max(a)}')
print(f'Eu sou o maior valor de a: {max(b)}')
print(f'Eu sou o maior valor de a: {max(c)}')
print(f'Dos valores, eu sou o maior {max(d.values())}')

print()

# exemplos de min():
print(f'Eu sou o menor valor de a: {min(a)}')
print(f'Eu sou o menor valor de a: {min(b)}')
print(f'Eu sou o menor valor de a: {min(c)}')
print(f'Dos valores, eu sou o menor {min(d.values())}')

print()
# Se quiséssemos saber qual a maior e menor palavra na lista?

palavras = ('agua', 'uva', 'granitos', 'futebol')

print(max(palavras, key=lambda palavra: len(palavra)))
print(min(palavras, key=lambda palavra: len(palavra)))

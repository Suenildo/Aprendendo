"""
Verificando o tempo de execução de uma comprehensio e um generators
"""


import time

# Generator Expression

gerador_inicio = time.time()
print(sum(num for num in range(100000)))
gerador_tempo = time.time() - gerador_inicio

# List Comprehension

lista_inicio = time.time()
print(sum(num for num in range(100000)))
lista_tempo = time.time() - lista_inicio

print(f'Generation Expression levou {gerador_tempo}')
print(f'List Comprehension levou {lista_tempo}')

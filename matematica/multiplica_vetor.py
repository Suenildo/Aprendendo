"""
Vamos multiplicar dois vetores utilizando o numpy.
"""

import numpy as np

v1 = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

v2 = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

dot_product = np.dot(v1[:, 0], v2)
print(dot_product)

print()
print('Nota explicativa:')

''' Nós vamos precisar multiplicar os vetores, sabemos que vetores
são matrizes, logo a regra de multiplicação de marizes se aplica
amultiplicação de vetores. Note que v1 e v2 são matrizes colunas,
dessse modo, não poderiam ser multiplicados pois possuem dimensões: 
v1 = 1 x 3 e v2 = 1 x 3.
As dimensões não atendem a condição para multplicação de matrizes,
então precisamos converter um dos vetores para um vetor linha, pois
assim teríamos as dimensões: 1 x 3 e 3 x 1. Satisfazendo a condição
para multiplicá-lo.
Para isso vamos usar a notação:
v1[:, 0] ou v2[:, 0], vejam os seus prints abaixo:
'''

print(f'Dimensões de v1 = {v1.shape}')
print(f'Dimensões de v2 = {v2.shape}')

print(f'Convertendo o vetor coluna para linha --> v1 = {v1[0:3, 0]}')
print(f'Convertendo o vetor coluna para linha --> v2 = {v2[:, 0]}')





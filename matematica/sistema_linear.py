"""
Vamos resolver sistemas lineares utilizando o numpy.
"""
import numpy as np


print('Calcule o valor de x e y no sistema:\n '
      '2x + 5y = 3 \n'
      ' 4x + 9y = 7 \n ')

# Vamos converter as equações para matrizes:
a = np.array([[2, 5], [4, 9]])
b = np.array([3, 7])

# resolvendo o sistema com numpy:
x, y = np.linalg.solve(a, b)
print(f'O valor de x é {x}.\n'
      f'O valor de y é {y}')

"""
Vamos resolver um sistema linear com três incógnitas.
"""

import numpy as np

print('Calcule o valor de x, y e z no sistema:\n'
      'x - 2y - 2z = -1\n'
      'x - y + z = -2\n'
      '2x + y + 3z = 1')

# Convertendo o sistema para matriz:
a = np.array([[1, -2, -2], [1, -1, 1], [2, 1, 3]])
b = np.array([-1, -2, 1])

# Resolvendo o Sistema:
x, y, z = np.linalg.solve(a, b)

print(f'O valor de x é {x} \n'
      f'O valor de y é {y}\n'
      f'O valor de z é {z}')

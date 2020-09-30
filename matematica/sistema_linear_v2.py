"""
Agora um de 4 incógnitas.
"""
import numpy as np

print('Calcule o valor de x, y, z e t no sistema:\n'
      '3x + 2y - 4z + t = 30\n'
      '2x + 3y + 3z + 2t = 150\n'
      '5x - 3y + z - 5t =140\n'
      'x + y + z + t = 60\n')

a = np.array([[3, 2, -4, 1], [2, 3, 3, 2], [5, -3, 1, -5], [1, 1, 1, 1]])
b = np.array([30, 150, 140, 60])

x, y, z, t = np.linalg.solve(a, b)

print(f'O valor de x é {x} \n'
      f'O valor de y é {y}\n'
      f'O valor de z é {z}\n'
      f'O valor de t é {t}')

print()
print('Outra manira de fazer:')
resultado = np.linalg.solve(a, b)
print(f'Os valores de x, y, z e t são: {resultado}')



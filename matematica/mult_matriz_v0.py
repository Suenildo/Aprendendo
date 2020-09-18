"""
Multiplicaremos as matrizes 'x' e 'y' usando dois métodos:
- loop for; e
- list comprehension
"""

x = [[1, 3, 6],
     [5, 2, 3],
     [1, 5, 2]]

y = [[6, 4, 2, 1],
     [2, 4, 5, 2],
     [4, 1, 5, 3]]

linhas_x = len(x)
colunas_x = len(x[0])
linhas_y = len(y)
colunas_y = len(y[0])

C = [[0 for linha in range(colunas_y)] for coluna in range(linhas_x)]

print(f'Matriz C = {C}')

for i in range(linhas_x):
    for j in range(colunas_y):
        for k in range(colunas_x):
            C[i][j] += x[i][k] * y[k][j]

print(f'O resultado de A x B é  C = {C}')

print()

resultado = [[sum(a * b for a, b in zip(x_linha, y_coluna)) for y_coluna in zip(*y)] for x_linha in x]

print(f'O resultado de A x B é  C = {resultado}')

"""
Vamos construir algumas matrizes sem utilização do numpy.
"""

#função que verifica se a matriz é identidade:


a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

cont = 0
cont1 = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j and a[i][j] == 1:
            cont += 1
        elif i != j and a[i][j] == 0:
            cont1 += 1

if cont == len(a) and cont1 == len(a) * len(a) - len(a):
    print('A matriz é identidade')
else:
    print('A matriz não é identidade')
"""
Neste exemplo de Multiplicação de Matrizes, vamos
fazer a multiplicação usando uma listcomprehencio, ao invés de
loops aninhados.
Tanto esse método, quanto o do exercício anterior, estão
corretos, entretanto, este é o método Pytônico.
"""

x = [[1, 3, 6],
     [5, 2, 3],
     [1, 5, 2]]

y = [[6, 4, 2, 1],
     [2, 4, 5, 2],
     [4, 1, 5, 3]]

resultado = [[sum(a*b for a,b in zip(x_linha, y_coluna)) for y_coluna in zip(*y)] for x_linha in x]

for r in resultado:
    print(r)

'''
lista = list(zip(x, y))
print(lista)
print(len(lista))

u = [a + b for a, b in lista]
print(u)

print('=*=' * 10)
s = list(zip(*y))
t = list(zip(*x))

print(s)
print(t)'''
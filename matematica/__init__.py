import numpy as np

'''a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.ndim)
print(a.shape)
print(len(a))  # retorna o tamanho da primeira linha

b = np.arange(0, 99, 5)
print(b)

print('=*=' * 10)
c = np.linspace(1, 10, 12)
# Ele colocará  12 elementos entre o 1 e o 10 (inclusiveis)
print(c)

print('=*=' * 10)
d = np.linspace(1, 10, 12, endpoint=False)
print(d)

print('=*=' * 10)
# Criando um array de "1"s
e = np.ones(10)
print(e)

print('=*=' * 10)
# Criando uma Matriz de "1" s com shape:
f = np.ones((5,5))
print(f)

print('=*=' * 10)
#Criando uma matriz de números aleatórios:
print("Criando uma matriz unidimensional de 6 elementos aleatórios entre 0 e 1")
g = np.random.rand(6)
print(g)

print('=*=' * 10)
print("Criando uma matriz multimensional de elementos aleatórios 3 x 3 entre 0 e 1")
h = np.random.rand(3, 3)
print(h)

print('=*=' * 10)
print('Criando matriz Identidade')
i = np.eye(5)
print(i)


print('=*=' * 10)
print('Criando uma matriz com uma diagonal a sua escolha')
j = np.diag(np.array([5, 9, 12, 0, 3]))
print(j)'''

x = [[1, 3, 6],
     [5, 2, 3],
     [1, 5, 2]]

y = [[6, 4, 2, 1],
     [2, 4, 5, 2],
     [4, 1, 5, 3]]

print("zip(*y)")
u = list(zip(*y))
print(u)

print()

print("for y_coluna in zip(*y)")
for u_colunas in u:
    print(u_colunas)

print()
print('=*=' * 15)

print("for x_linha in x")
for c_linha in x:
    print(c_linha)

print()
print('=*=' * 15)

resultado = [[sum(a * b for a, b in zip(x_linha, y_coluna)) for y_coluna in zip(*y)] for x_linha in x]

for r in resultado:
    print(r)

print()
print('=*=' * 15)

print('sum')
a = sum(y, x)
print(a)



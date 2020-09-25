
x = [[1, 3, 6], [2, 3, 1], [2, 5, 1]]
y = [6, 4, 2]

d1 = list(zip(x, y))
print(d1)

d2 = [a * b for a, b in zip(x, y)]
print(d2)

resultado = sum(d2)
print(resultado)

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


n = int(input('Digite quantos números você quer na sequência: '))

for indice, x in enumerate(fibonacci()):
    if indice == n:
        break
    print('(', x, ')', end=' - ')

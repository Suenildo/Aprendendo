
def fatorial(n):
    if n == 0:
        return 1
    fat = n
    i = n - 1
    while i >= 1:
        fat *= i
        i -= 1
    return fat

print(fatorial(0))


def fatorial_rec(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * fatorial_rec(m - 1)


print(fatorial_rec(4))


def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


fat = fatorial(int(input('Digite um número inteiro: ')))

print(fat)

print('=*=' * 15)


# Agora com recursividade:

def fatorial_1(n):
    if n == 0 or n == 1:
        return 1
    return fatorial_1(n - 1) * n


print(fatorial_1(0))
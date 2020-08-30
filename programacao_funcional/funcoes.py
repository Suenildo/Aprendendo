
# Função com recursividade

# Observe a funçãp sem recursividade:

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
    return fatorial_1(n-1) * n

print(fatorial_1(5))
'''def quadrado():
    print(2 * 2)


valor = quadrado()
print(f'Este é o retorno --> {valor}')

print('=+=' * 10)

def quadrado_1():
    return (2 * 2)


valor1 = quadrado_1()
print(f'Este é o retorno --> {valor1}')'''


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
    return fatorial_1(n - 1) * n


print(fatorial_1(0))

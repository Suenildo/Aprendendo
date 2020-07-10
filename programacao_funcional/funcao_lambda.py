"""
O que essa função faz:
Uma expressão (lambda) permite escrever funções anônimas/sem-nome
usando apenas uma linha de código. Onde var1, var2, ..., varN
são variáveis que representam o argumento da função e expr é
qualquer expressão válida em Python envolvendo essas variáveis.
O resultado é uma nova expressão expr_ret.
"""
valor = [1, 2, 3, 4, 5]
valor2 = [1, 2, 3, 4, 5]


print('Dobrando e triplicando o valor dos elementos da lista')
valor_dobro = map(lambda i: i*2, valor)
valor_dobro = list(valor_dobro)
print(valor_dobro)
valor_triplo = map(lambda j: j*3, valor)
valor_triplo = list(valor_triplo)
print(valor_triplo)

print()
print('Elevando ao quadrado o valor dos elementos da lista')
valor_quadrado = map(lambda i: i**2, valor2)
valor_quadrado = list(valor_quadrado)
print(valor_quadrado)
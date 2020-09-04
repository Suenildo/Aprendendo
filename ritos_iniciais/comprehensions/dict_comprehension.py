"""
Dictionary comprehension é um método para transformar um dicionário
em outro dicionário. Durante essa transformação, os itens do dicionário
original podem ser incluídos condicionalmente no novo dicionário e cada
item pode ser transformado conforme necessário.
"""

# Criando um dicionário:
dicionario_01 = {'bola': 3, 'raquete': 5, 'carrinho': 7, 'boneco': 10}

# Vamos aumentar em 50% os preços do itens (chaves) do dicionário:

dic_aumento = {chave: valor * 1.5 for chave, valor in dicionario_01.items()}

print(dic_aumento)
# Perceba que não alteramos o dicioário original.

# Vamos uma lista  com salários e dar um aumento mostrando o salário anterior:
# O aumento será de 30%

salarios = [1000.00, 2000.00, 2500.00, 3200.00]
salarios_com_aumento = {valor: valor * 1.3 for valor in salarios}
print(salarios_com_aumento)

# salarios, poderia ser: tupla, set, lista ou dicionário.
# Não pode haver repetição de chaves, portanto cuidado com as coleções.

# Com string:
string = 'suenildo'
valores = [1, 2, 3, 4, 5, 6, 7, 8]

unindo = {string[i]: valores[i] for i in range(0, len(string))}
print(unindo)

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8)

classifica = {num: ('Par' if num % 2 == 0 else 'Impar') for num in numeros}

print(classifica)

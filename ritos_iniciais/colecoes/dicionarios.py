"""
Dicionários, são estruturas de dados que implementam mapeamentos,
ou seja, é uma  associações entre uma dupla de elementos.
O primeiro elemento da dupla é chamado de chave e o segundo  de valor.
- dicionários não são indexados
- dicionários são acessados pelas suas chaves
"""
# Criando um dicionário vazio:

dicionario = {}
print(type(dicionario))

'''
Tabela de preços dos doces
+-------------+----------+
|   Produto   |  preço   |   
+-------------+----------+
|  bananada   | R$ 2,00  |  
+-------------+----------+
|  goiabada   | R$ 3,00  |  
+-------------+----------+
podemos representar a tabela com um dicionário.
'''

precos = {'bananada': 2.00,
          'goiabada': 3.00}

print(precos)

# Maneira menos peculiar de construir um dicionário:
precos_construtor = dict(bananada=2.00, goiabada=3.00)

print(precos_construtor)

print()

# Acessando pela chave:
print('Acessando pelas chaves:')
print(precos["bananada"])
print(precos['goiabada'])

print()
# Acessando através do "get":
print('Acessando com o get:')
print(precos.get('goiabada'))

print()

'''
No caso em que você acessa pelo "get", e, a chave não exista,
ela retornará None:
'''
print(precos.get('cajuada'))

print()
# criando uma chave e valor
precos_construtor['cajuada'] = 2.50
print(precos_construtor)

print()

print('--' * 13)
print('Outras maneiras de acesso:')
print('--' * 13)

print()

dias_dos_meses = {'Janeiro': 31, 'Fevereiro': 28, 'Março': 31, 'Abril': 30}

print('Imprimindo um dicionário de chaves:')
print(dias_dos_meses.keys())
print()

print('Imprimindo um dicionário de valores:')
print(dias_dos_meses.values())

print()

for chave in dias_dos_meses.keys():
    print(chave)

for valor in dias_dos_meses.values():
    print(valor)

print()
print('Mais algumas funções com dicionários:')

soma = sum(dias_dos_meses.values())
valor_maximo = max(dias_dos_meses.values())
valor_minimo = min(dias_dos_meses.values())
tamanho = len(dias_dos_meses)

print(f'O valor da soma dos dias mostrados é: {soma}')
print(f'O valor máximo dos valores é: {valor_maximo}')
print(f'O valor mínimo dos valores é: {valor_minimo}')
print(f'A quantidade de intens no dicionário é: {tamanho}')

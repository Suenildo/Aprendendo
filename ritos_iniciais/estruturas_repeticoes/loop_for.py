"""
O laop for vai permitir percorrer todos os itens de uma coleção e,
para cada um deles, executar o bloco de código declarado no laço.
Sintaxe:

for itens in iterável:
    comandos

"""

objetos = ['bola', 'pião', 'livro', 'caneta']

for itens in objetos:
    print(itens)
print()

# Podemos trabalhar o for com o  else.
carros = ('fusca', 'gol', 'belina')
for itens in carros:
    print(itens)
else:
    print("Todos os itens foram impressos")
# A cláusula else é executada após o loop ser concluído.


nome = 'SUENILDO'
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
for indice in enumerate(nome):
    print(indice)

print()

idiomas = {"Português": "Brasil", "Inglês": "Canada", "Francês": "França", "Alemão": "Alemanha"}
for chave, valor in idiomas.items():
    print(chave, "->", valor)

print()

# Vai retornar o código na tabela ascii
for letra in 'Python':
    cod = ord(letra)
    print(cod, '--', letra)

print()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, ' = ', x, 'x', n//x)
            break
    else:
        print(n, 'é um número primo')

''' O else é executado, toda vez que a condição if
não é verdadeira
'''


"""
O loop while executa um conjunto de instruções enquanto uma condição
é verdadeira. Quando essa condição passa a ser falsa, o loop é interrompida.
"""

count = 0
while count <= 5:
    print(count)
    count += 1

print()

# Podemos usar o "else" com o while, como foi usado no "for".
i = 2
while i < 6:
    print(i)
    i += 1
else:
    print("Acabou o while")




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


# Vamos usar acumuladores:

contador = 1
acumulador = 0
while contador <= 6:
    numero = int(input(f'Digite o {contador}º número: '))
    acumulador = acumulador + numero
    contador += 1

print(f'O valor acumulado foi: {acumulador}')

# Se eu quiser saber a média aritmética:

print(f' A média aritmético dos valores digitados é: {acumulador / (contador - 1)}')

# Repetições aninhadas:

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{tabuada} x {numero} = {tabuada * numero}')
        numero += 1
    tabuada += 1
''' Exemplo tirado do livrro: 
Introdução a Programação com Python
Nilo Ney Coutinho Meneses
Novatec'''
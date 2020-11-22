"""
Vamos fazer um exercício utilizando:
if, elif e else.
O primeiro modo é mais truculento, o segundo, mais elegante.
"""
print('Primeiro modo')
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if b > a:
    if c > b:
        print(c, " é o maior número.")
    else:
        print(b, " é o maior número. ")
else:
    if c > a:
        print(c, " é o maior número. ")
    else:
        print(a, " é o maior número. ")

print()
print('Segundo modo')

d = int(input("Digite o primeiro número: "))
e = int(input("Digite o segundo número: "))
f = int(input("Digite o terceiro número: "))

numero_maior = d
if e > numero_maior:
    numero_maior = e
if f > numero_maior:
    numero_maior = f
print(numero_maior, " é o maior número. ")

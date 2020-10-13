"""
Utilizando um acumulador.
"""

contador = 1
acumulador = 0
while contador <= 6:
    numero = int(input(f'Digite o {contador}º número: '))
    acumulador = acumulador + numero
    contador += 1

print(f'O valor acumulado foi: {acumulador}')

# Se eu quiser saber a média aritmética:

print(f' A média aritmética dos valores digitados é: {acumulador / (contador - 1)}')
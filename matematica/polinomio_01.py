"""
Resolução de polinômio usando programação.
"""

from math import pow

print('Dado o polinômio: aX^3 + bX^2 + cX + d:')

coeficientes = []

for i in range(0, 4):
    valores = int(input('Digite o coeficiente: '))
    coeficientes.append(valores)

x = int(input('Digite o valor da variável X: '))

termo = 0

expoente = 3  # valor do meu maior expoente do polinômio.

for i in range(0, 3):
    while expoente > 0:
        termo = termo + (coeficientes[i] * pow(x, expoente))
        break
    expoente = expoente - 1

termo = termo + coeficientes[3]

print('O valor do polinômio é: ', termo)

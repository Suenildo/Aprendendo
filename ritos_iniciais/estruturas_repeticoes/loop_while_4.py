"""
Repetições aninhadas:
"""

tabuada = 1
print(f'Tabuada de 1')
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{tabuada} x {numero} = {tabuada * numero}')
        numero += 1
    tabuada += 1
    print()
    print('=*=' * 5)
    if tabuada < 11:
        print(f'Tabuada de {tabuada}')


''' Exemplo tirado do livrro: 
Introdução a Programação com Python
Nilo Ney Coutinho Meneses
Novatec.
Sendo modificado por mim.
'''
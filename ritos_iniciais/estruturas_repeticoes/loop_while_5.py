"""
Utilizando while para jogo de acerto e erro.
"""

from random import randint

valor = randint(1, 10)
while True:
    tentativa = int(input('Tente acertar o número: '))
    if tentativa == valor:
        print(f'Você acertou, o número era:  {valor}')
        break
    else:
        print('Tente um menor' if tentativa > valor else 'Tente um maior')
print('Game over, obrigado por jogar.')

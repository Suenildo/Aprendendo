from random import choice


def heroi(nome):
    def arma():
        return choice(('Martelo ', 'escudo ', 'lança'))

    return nome + arma()

# Chamada direta
print(heroi('super um --> '))
print(heroi('super dois --> '))

print()

# Chamada indireta
a = heroi('Super Nelson ==> ')
print(a)

"""
Decorators é um design pattern (design padrão) que permite alterar
o comportamento de uma função, classe ou método, dinamicamente.
"""


class Objetivo(object):
    def __init__(self, f):
        print('Qual o seu nome e o que você faz?')
        self.f = f

    def __call__(self, *args):
        self.f(args[0].upper())
        print('Eu salvo o mundo')


@Objetivo
def heroi(nome):
    print(f'Nome: {nome}')


heroi('Super Homem')
print()
heroi('Homem de Ferro')
print()
heroi('Hulk')
print()
heroi('Mulher Maravilha')

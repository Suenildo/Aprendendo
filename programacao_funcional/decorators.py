"""
Decorators é um design pattern (design padrão) que permite alterar
o comportamento de uma função, classe ou método, dinamicamente.
"""


class Matematica(object):
    def __init__(self, f):
        print('Qual o seu nome e o que você faz?')
        self.f = f

    def __call__(self, *args):
        self.f(args[0].upper())
        print('Sou uma operação matemática')


@Matematica
def operacao(nome):
    print(f'Nome: {nome}')


operacao('Soma')
print()
operacao('Subtração')
print()
operacao('Multiplicação')
print()
operacao('Divisão')

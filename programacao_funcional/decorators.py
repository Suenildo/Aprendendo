"""
Decorators é um design pattern (design padrão) que permite alterar
o comportamento de uma função, classe ou método, dinamicamente.
"""


# Vamos criar uma classe decoradora:
class Matematica(object):
    def __init__(self, f):
        print('Qual o seu nome e o que você faz?')
        self.f = f

    def __call__(self, *args):
        self.f(args[0].upper())
        print('Sou uma operação matemática')


@Matematica  # Decorators
def operacao(nome):
    print(f'Nome: {nome}')


operacao('Soma')
print()
operacao('Subtração')
print()
operacao('Multiplicação')
print()
operacao('Divisão')

print()
print()


# Exemplo com uma função:

def titulo(funcao):
    def entitular(nome):
        return funcao(nome).title()  # aqui o parâmetro é modificado

    return entitular  # Aqui é o retorno da função principal, chamando a função secundária


@titulo  # Decorators
def palavra(nome):
    return 'adriana é jogadora de video game'


#  O decorador será aplicado em tuda a função

print(palavra('otimo'))

'''
Caso você não saiba se suas futuras funções que serão decoradas
vão possuir um, dois ou mais parâmetros, você pode generalizar o
número de parâmetros com o ((Decorator Pattern))

exemplo

def titulo(funcao):
    def entitular(*args, **kwargs):
        return funcao(nome).title() 

    return entitular  
'''
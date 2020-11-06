"""

"""
from functools import wraps

def decoracao(funcao):
    def decorador(*args, **kwargs):
        """ Sou uma função interna"""
        print(f'Aqui eu chamo a função: {funcao.__name__}')
        print(f'Chamando a documentação: {funcao.__doc__}')
        print(f'Argumentos: {args}')
        print(f'Argumentos nomeados: {kwargs}')
        resultado = funcao(*args, **kwargs)

    return decorador


@decoracao
def multiplica(a, b):
    """ Multiplico números"""
    return a * b

@decoracao
def soma(c, d):
    """ Somo números"""
    return c + d


if __name__ == '__main__':
    # print(multiplica(3, 6))
    # print(soma(3, d=5))
    print(soma.__name__)
    print(soma.__doc__)

print()
print('=*=' * 20)
'''Reparem nesse exemplo que as informações pedidas nos prints
não são verdadeiras, isso nós resolveremos abaixo'''


def decora(funcao):
    @wraps(funcao)  # Solução do Problema.
    def decorador(*args, **kwargs):
        """ Sou uma função interna"""
        print(f'Aqui eu chamo a função: {funcao.__name__}')
        print(f'Chamando a documentação: {funcao.__doc__}')
        print(f'Argumentos: {args}')
        print(f'Argumentos nomeados: {kwargs}')

    return decorador


@decora
def mult(a, b):
    """ Multiplico números"""
    return a * b

@decora
def som(c, d):
    """ Somo números"""
    return c + d


if __name__ == '__main__':
    # print(mult(3, 6))
    # print(som(3, d=5))
    print(som.__name__)
    print(som.__doc__)

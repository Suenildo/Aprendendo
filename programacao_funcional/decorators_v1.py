def decoracao(funcao):
    def decorador(*args, **kwargs):
        print(f'Aqui eu chamo a função: {funcao.__name__}')
        print(f'Argumentos: {args}')
        print(f'Argumentos nomeados: {kwargs}')
        resultado = funcao(*args, **kwargs)
        print(f'Resultado da chamada da função decorada: {resultado}')
        return resultado

    return decorador


@decoracao
def multiplica(a, b):
    return a * b

@decoracao
def soma(c, d):
    return c + d


if __name__ == '__main__':
    print(multiplica(3, 6))
    print(soma(3, d=5))

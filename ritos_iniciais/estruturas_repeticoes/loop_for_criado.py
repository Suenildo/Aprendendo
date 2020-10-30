"""
Vamos criar um loop simulando um for
"""


def loop_criado(iteravel):
    elemento = iter(iteravel)
    while True:
        try:
            print(next(elemento))
        except StopIteration:
            break


loop_criado('Seu nome')
pares = [0, 2, 4, 6, 8, 10]
loop_criado(pares)

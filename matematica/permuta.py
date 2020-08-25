"""
Em combinatória, o termo permutação tem um significado tradicional,
que é usado para incluir listas ordenadas sem repetição, mas não
exaustiva (portanto com menos elementos do que o máximo possível).

O conceito de permutação expressa a ideia de que objetos
distintos podem ser arranjados em inúmeras ordens diferentes.

https://pt.wikipedia.org/wiki/Permuta%C3%A7%C3%A3o
"""


def permuta_letras(str):
    if len(str) == 0:
        return ['']

    lista_atual = permuta_letras(str[1:len(str)])
    proxima_lista = []

    # Percorrendo a matriz formada pelas permutações
    for i in range(0, len(lista_atual)):
        for j in range(0, len(str)):
            nova_palavra = lista_atual[i][0:j] + str[0] + lista_atual[i][j:len(str) - 1]
            if nova_palavra not in proxima_lista:
                proxima_lista.append(nova_palavra)
    return proxima_lista


print(permuta_letras(str(input('Digite a palavra a ser permutada, sem espaços: '))))


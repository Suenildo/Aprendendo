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
    for i in range(len(lista_atual)):  # Poderia se "Range(0, len(lista_atual))
        for j in range(len(str)):  # Poderia se "Range(0, len(str))
            nova_palavra = lista_atual[i][0:j] + str[0] + lista_atual[i][j:len(str) - 1]
            if nova_palavra not in proxima_lista:
                proxima_lista.append(nova_palavra)
    return proxima_lista


print(permuta_letras('MAR'))

# print(permuta_letras(str(input('Digite a palavra a ser permutada, sem espaços: '))))

"""
print()
print()


print('Outros algoritmos de permutação:')


''' Os exemplos abaixo foram pegos no site:
https://wdrblog.wordpress.com/2017/11/26/algoritmo-de-permutacao-ou-anagrama-em-python/
'''
# Programa sem backtracking


def permuta(s, s1=''):
    if len(s) == 0:
        print(s1)
    else:
        for i in range(len(s)):
            permuta(s[:i] + s[(i + 1):], s1 + s[i])

permuta('ABCD')

print()
print()


# Programa com backtracking



def perm(s, i=0):
    if i == len(s) - 1:
        print(s)
    else:
        for j in range(i, len(s)):
            t = s
            s = s[j] + s[:j] + s[(j + 1):]
            perm(s, i + 1)
            s = t


perm('ABCD')"""
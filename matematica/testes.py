def permuta_letras(palavra):
    if len(palavra) == 0:
        return ['']

    lista_atual = permuta_letras(palavra[1:len(palavra)])
    # proxima_lista = []
    print(lista_atual)


u = permuta_letras(input('Digite a palavra a ser permutada, sem espaços: '))
print(u)

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


perm('ABCD')
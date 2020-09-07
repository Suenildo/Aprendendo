def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite o número que você quer o fatorial: '))

mostra = str(input('Para ver o cálculo digite s ou n '))
if mostra in 'sS':
    mostra = True
else:
    mostra = False

print(fatorial(n, mostra))

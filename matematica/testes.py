def permuta_letras(palavra):
    if len(palavra) == 0:
        return ['']

    lista_atual = permuta_letras(palavra[1:len(palavra)])
    # proxima_lista = []
    print(lista_atual)


u = permuta_letras(input('Digite a palavra a ser permutada, sem espaços: '))
print(u)


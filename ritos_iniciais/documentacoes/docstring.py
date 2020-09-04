"""
Uma docstring é uma string literal presente na primeira linha da
definição de um módulo, classe ou função. O docstring de qualquer
objeto pode ser acessado através de um atributo especial chamado __doc__.
"""


# Um exemplo de docstrig de uma função:

def soma_dois_numeros(a, b):
    """
    Função que soma dois números
    :param a: primeiro número a ser somado
    :param b: segundo número a ser somado
    :return: retorma a soma dos dois números
    """
    return a + b


a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print(soma_dois_numeros(a, b))

print(soma_dois_numeros.__doc__)
print(help(soma_dois_numeros))

# Acostume-se a documentar tudo que você faz.

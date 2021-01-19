"""
Obsessão por Primitivos:
A obsessão por primitivos é caracterizada por estruturas que podem ser
representadas por objetos concretos, mas ela é representada por um tipo
"primitivo" da linguagem.

fonte: https://www.youtube.com/watch?v=NtZY3AmsBSk&feature=youtu.be
"""

from collections import namedtuple

dados = [
    {
        'nome': 'Maria',
        'sobrenome': 'Silva',
        'telefone': {'residencial': '1111-1111', 'movel': '999-999-999'},
        'ddd': 19,
    },
]

# Notem a dificuldade de acessar alguns dados dentro do dicionário dados

nomes_completos = [f"{dado['nome']} {dado['sobrenome']}" for dado in dados]

print(nomes_completos)


print('*=*' * 10)

# Uma das maneiras de facilitar o acesso, é a namedtupla

pessoa = namedtuple('pessoa', 'nome sobrenome telefone ddd')

dados_1 = [
    pessoa('Gilson', 'Santos', {'residencial': '1111-1111', 'movel': '9999-9999'}, 19),
    pessoa('Marcio', 'Mendes', {'residencial': '1112-1111', 'movel': '9998-9999'}, 21),
]

gilson = dados_1[0]
# ou:
# gilson =  pessoa('Gilson', 'Santos', {'residencial': '1111-1111', 'movel': '9999-9999'}, 19),
print(gilson.nome, gilson.sobrenome)

p = pessoa('Sofia', 'Sousa', {}, 99)
print(p)


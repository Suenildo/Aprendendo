"""
O Default Dict, Retorna um novo objeto semelhante ao dicionário.
defaultdict é uma subclasse da classe dict interna. Ele substitui
um método e adiciona uma variável de instância gravável.
A funcionalidade restante é a mesma da classe dict.

class collections.defaultdict([default_factory[, ...]])

O primeiro argumento fornece o valor inicial para o atributo
default_factory; o padrão é Nenhum. Todos os argumentos restantes
são tratados da mesma forma como se fossem passados para o construtor dict,
incluindo argumentos de palavras-chave
"""
from collections import defaultdict

''' Caso você tente acessar uma chave inexistente em um dicionário
comum, ele apresentará KeyErro, mas com esse tipo de construção,
hora apresentado, isso não ocorre.'''

dicionario = defaultdict(lambda: 0)

# Vamos adicionar um elemento no dicionário:]
dicionario['esporte'] = 'futebol'

''' Se você mostrar a saída, ficaria:
    defaultdict(<function <lambda> at 0x016277C0>, {'esporte': 'futebol'})'''

print(dicionario)

print()

# E se tentarmos achar uma chave que não existe?
print(dicionario['brincadeira'])
print(dicionario)

# Note que ele não deu erro e sim adicionou um novo elemento, chace/valor

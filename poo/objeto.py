"""
Objeto em ciência da computação, é uma referência a um local
da memória que possui um valor. Um objeto pode ser uma variável,
função, ou estrutura de dados. Em programação orientada a objetos,
a palavra objeto refere-se a um "molde"/classe, que passa a existir
a partir de uma instância da classe

Origem: Wikipédia, a enciclopédia livre.
"""

# Em python, tudo é um objeto
lista_vogais = ['a', 'e', 'i', 'o', 'u']
print(type(lista_vogais))
# podemos ver que 'lista_vogais' é um objeto instanciado na classe 'list'

class RevistaQuadrinhos():
    def __init__(self, tipo, titulo):
        self.tipo = tipo
        self.titulo = titulo

    def imprime(self, tipo, titulo):
        print(f'Revista do tipo {tipo} com o título {titulo}')

revistinha = RevistaQuadrinhos('Heróis', 'Homem Aranha')

print(type(revistinha))
# podemos ver que 'revistinha' é um objeto instanciado na classe 'RevistaQuadrinhos'

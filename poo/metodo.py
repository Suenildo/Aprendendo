"""
Os métodos determinam o comportamento dos objetos de uma classe e
são análogos às funções ou procedimentos da programação estruturada.

Origem: Wikipédia, a enciclopédia livre.
"""


class RevistaQuadrinhos():
    def __init__(self, tipo, titulo):
        self.tipo = tipo
        self.titulo = titulo

    def imprime(self, tipo, titulo):
        print(f'Revista do tipo {tipo} com o título {titulo}')


revistinha = RevistaQuadrinhos('Heróis', 'Homem Aranha')

# Vamos através do método 'imprime' mostrar os atributos de 'revistinha.
revistinha.imprime('Heróis', 'Homem Aranha')

print(type(revistinha.imprime))  # Aqui fica claro que 'imprime é um método

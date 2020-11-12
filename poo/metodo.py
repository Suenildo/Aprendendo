"""
Os métodos determinam o comportamento dos objetos de uma classe e
são análogos às funções ou procedimentos da programação estruturada.

Origem: Wikipédia, a enciclopédia livre.

- Métodos de Instância:
  - Métodos encontrados dentro da classe, São métodos
    vinculados as Instâncias da Classe.

- Métodos de Classe:
  - Para criar um método de classe, é preciso usar um decorator.
    @classmethod
  def nome_do_metodo(cls):
      xxx
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

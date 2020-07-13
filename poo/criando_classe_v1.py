"""
Criaremos, nesse código, os atributos de forma
correta, passados como parâmetros.
"""

class RevistaQuadrinhos():
    def __init__(self, tipo, titulo):
        self.tipo = tipo
        self.titulo = titulo

    def imprime(self, tipo, titulo):
        print(f'Revista do tipo {tipo} com o título {titulo}')

revistinha = RevistaQuadrinhos('Heróis', 'Homem Aranha')

revistinha.imprime('Heróis', 'Homem Aranha')
print("-*-" * 16)
revistinha1 = RevistaQuadrinhos('Infantil', 'Turma da Mônica')

revistinha1.imprime('Infantil', 'Turma da Mõnica')
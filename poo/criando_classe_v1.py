"""
Criaremos, nesse código, os atributos de forma
correta, passados como parâmetros.
"""


class RevistaQuadrinhos():
    def __init__(self, tipo, titulo): #  Método construtor
        self.tipo = tipo
        self.titulo = titulo

    def imprime(self, tipo, titulo):
        print(f'Revista do tipo {tipo} com o título {titulo}')

# Criando um objeto
revistinha = RevistaQuadrinhos('Heróis', 'Homem Aranha')

# Chamada do método imprime, com os parâmetros do objeto instanciado:
revistinha.imprime('Heróis', 'Homem Aranha')
print()
print("-*-" * 16)
print()

# Criando(instanciando) outro objeto:
revistinha1 = RevistaQuadrinhos('Infantil', 'Turma da Mônica')

# Chamada do método impreme:
revistinha1.imprime('Infantil', 'Turma da Mõnica')

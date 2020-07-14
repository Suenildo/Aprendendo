"""
Herança é um princípio de orientação a objetos, que permite que
classes compartilhem atributos e métodos, através de "heranças".
Ela é usada na intenção de reaproveitar código ou comportamento
generalizado ou especializar operações ou atributos.

Origem: Wikipédia, a enciclopédia livre.
"""


class Revistas():
    def __init__(self):
        pass


class Quadrinhos(Revistas):
    def __init__(self, tipo, estilo, titulo):
        Revistas.__init__(self)
        self.tipo = tipo
        self.estilo = estilo
        self.titulo = titulo
        print('criada subclasse')

    def imprime(self, tipo, estilo, titulo):
        print(f'Revista do tipo {tipo} do estilo {estilo} com o título {titulo}')


ciclope = Quadrinhos('Quadrinhos', 'herois', 'Homem de ferro')

ciclope.imprime('Quadrinhos', 'herois', 'Homem de ferro')

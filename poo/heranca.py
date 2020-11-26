"""
----Herança ou Inheritance----

Herança é um princípio de orientação a objetos, que permite que
classes compartilhem atributos e métodos, através de "heranças".
Ela é usada na intenção de reaproveitar código ou comportamento
generalizado ou especializar operações ou atributos.

Origem: Wikipédia, a enciclopédia livre.
"""


class Revistas:
    def __init__(self):
        print('criado o objeto')


class Quadrinhos(Revistas):
    def __init__(self, tipo, estilo, titulo):
        Revistas.__init__(self)
        self.tipo = tipo
        self.estilo = estilo
        self.titulo = titulo
        print('criada subclasse')

    def imprime(self, tipo, estilo, titulo):
        print(f'Revista do tipo {tipo} do estilo {estilo} com o título {titulo}')


revista_do_tipo = input('Digite o tipo de revista: ')
revista_estilo = input('Digite o estilo de revista: ')
titulo_revista = input('Digite o título da revista: ')

revista1 = Quadrinhos(revista_do_tipo, revista_estilo, titulo_revista)

revista1.imprime(revista_do_tipo, revista_estilo, titulo_revista)

print(type(revista1))

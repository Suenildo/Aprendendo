"""
Temos que tomar cuidado co herança múltipla.
No exemplo abaixo, veremos um problema que pode ocorrer.
Por que ele somente executa o método greet da classe English?

The so called “left-right” fashion
No Python, em casos de herança múltipla, a prioridade é definida
da esquerda para a direita.

Por convenção, programadores Python implementam herança múltipla
de forma bem granular, usando Mixins! O código do Django tem
muitos bons exemplos disso.

fonte:
https://medium.com/rafaeltardivo/python-e-heran%C3%A7a-m%C3%BAltipla-como-funciona-876db0449efe
"""


#  Exemplo:

class English(object):
    def greet(self):
        print('Hi!')


class Portuguese(object):
    def greet(self):
        print('Oi!')


class Bilingual(English, Portuguese):
    pass


if __name__ == '__main__':
    Bilingual().greet()

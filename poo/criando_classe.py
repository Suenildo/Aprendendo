"""
Em orientação a objetos, uma classe é uma descrição que
abstrai um conjunto de objetos com características similares.
Mais formalmente, é um conceito que encapsula abstrações de
dados e procedimentos que descrevem o conteúdo e o comportamento
de entidades do mundo real, representadas por objetos

Origem: Wikipédia, a enciclopédia livre.
"""

class Revista():
    """
    Criada a classe 'Revista' com a palavra reservada 'class'.
    Para inicializar um objeto, vamos char o construtor '__init__'.
    Em seguida, criar dois atributos: 'titulo' e 'assunto'.
    Por último o método 'imprime'.
    """
    def __init__(self):
        self.titulo = 'Programação Python'
        self.assunto = 'Informática'
        print('Aqui o construtor cria o objeto')
    def imprime(self):
        print(f'Foi criado o objeto revista {self.titulo} '
              f'cujo assunto é {self.assunto}')

revista1 = Revista()

print(type(revista1))

print(revista1.titulo)

revista1.imprime()

'''
Os atributos:
- titulo e
-assunto
foram criados de uma forma que não é muito recomendada,
os mesmos deveriam ter sido passados como parâmetros. '''

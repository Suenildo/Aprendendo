class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        """
        método de instância
        :return: pedacos - 1
        """
        self.pedacos -= 1

    @classmethod
    def muda_tamanho(cls, pedacos):  # (*)
        cls.pedacos = pedacos

    '''
    Nós podemos alterar a quantidade de pedaços da Pizza através do "cls",
    e, fazendo isso vamos alterar para todas as instãncias. Fazemos isso 
    com um classmethod, vejamos o exemplo (*). 
    '''


    @staticmethod
    def ingredientes():
        return 'molho de tomate, queijo e oregano'

#  Vamos instanciar um sabor de pizza:
mussarela = Pizza('Mussarela')

print(mussarela.sabor)

#   Buscando um atributo da classe
#   Este aparece em todas as instâncias
print(mussarela.pedacos)

#   Vamos pegar um pedaço da pizza de mussarela
mussarela.pegar_pedaco()
print(mussarela.pedacos)  # ficaremos com 7 pedaços

#   Reparem que a Pizza, no seu escopo global, continua com 8 pedaços
print(Pizza.pedacos)

print(Pizza.ingredientes())
print(mussarela.ingredientes())



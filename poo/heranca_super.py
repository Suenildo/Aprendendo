class Joia:
    def __init__(self, nome, composicao):
        self.__nome = nome
        self.__composicao = composicao

    def tipo_de_brilho(self, brilho):
        print(f'O padrão do(a) {self.__nome} é {brilho}.')


class Pedra_preciosa(Joia):

    def __init__(self, nome, composicao, cor):
        # Joia.__init__(self, nome, composicao)  # Método não correto
        super().__init__(nome, composicao)  # Método correto
        self.__composicao = composicao


esmeralda = Pedra_preciosa('esmeralda', 'mineral', 'verde')
esmeralda.tipo_de_brilho('esverdeado')

'''
com o super(), se pode fazer acesso a qualquer
elemento da Classe Pai
'''
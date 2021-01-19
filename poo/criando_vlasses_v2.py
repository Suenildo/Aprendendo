class Fila:
    """
    Abstração de qualquer tipo de fila:
        - farmácia
        - banco
        - ...
    """

    #  Tudo feito aqui, estará em todas as instâncias
    c_fila = []

    @classmethod
    def c_entrar(cls, obj):  # O cls vai estar em um escopo global
        cls.c_fila.append(obj)
        print(cls.c_fila)

    # A partir daqui só vai ser acessível através de uma  instanciação

    def __init__(self):
        self.s_fila = []

    def s_entrar(self, obj):   # O self vai estar somente em uma instância específica
        self.s_fila.append(obj)
        print(self.s_fila)

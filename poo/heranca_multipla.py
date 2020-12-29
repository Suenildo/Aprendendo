"""
Herança múltipma, nada mais é do que a capacidade de
Uma determinada Classe, herdar características de mais
de uma classe.

A herança multipla pode ser feita das seguintes formas:
 - Multiderivação Direta
 - multiderivação Indireta
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Instanciando e testando:

baleia = Aquatico('Moob')
print(baleia.nadar())
print(baleia.cumprimentar())

print()

tatu = Terrestre('Tata')
print(tatu.andar())
print(tatu.cumprimentar())

print()

wily = Pinguim('Wily')
print(wily.andar())
print(wily.nadar())
print(wily.cumprimentar())

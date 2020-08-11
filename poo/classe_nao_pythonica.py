"""
Vamos criar uma classe de um modo não pythonico, só para
mostar alguns tópicos.
"""


class Animal:  # Criada a classe sem a colocação dos parênteses no final
    def __init__(animal, especie, genero, locomocao, nome):
        # Ao invés do self, chamaremos de animal
        animal.especie = especie
        animal.genero = genero
        animal.numero_de_patas = locomocao
        animal.nome = nome

    def locomocao(animal):
        print(f'Eu ando sobre {animal.numero_de_patas} patas')

    def prenha(animal):
        if animal.genero.lower()[0] == 'm':
            print('Machos não emprenham')
            return
        print('prenha')


cao = Animal('canino', 'm', 4, 'joe')
cao.locomocao()
cao.prenha()

# Não trabalhe dessa forma
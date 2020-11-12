"""
Vamos cria uma classe com um contador
"""


class Cliente:
    contador_id = 0

    def __init__(self, nome, cpf, rg):
        self.id = Cliente.contador_id + 1
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        Cliente.contador_id = self.id

    def imprime(self, nome, cpf, rg):
        print(f'Nome: {nome}')
        print(f'CPF: {cpf}')
        print(f'RG: {rg}')
        print(f'ID: {Cliente.contador_id}')




a = input('Digite o nome do novo cliente: ')
b = input('Digite o CPF do novo cliente: ')
c = input('Digite o RG do novo cliente: ')

cliente_01 = Cliente(a, b, c)


cliente_01.imprime(a, b, c)


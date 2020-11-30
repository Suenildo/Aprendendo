"""
Usaremos nesse arquivos, os métodos:
get e set, para depois mostrarmos a forma Puthonica de se fazer.
"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente{self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Silvio', 2000, 3000)
conta2 = Conta('Silvia', 1000, 5000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é: {soma}')

print()
print('Vamos alterar o limite de conta1')
#  Dados antes da alteraçã:
print(conta1.__dict__)

print()
#  Alteração
conta1.set_limite(6000)

print()
print('Dados alterados:')
print(conta1.__dict__)

'''
# Usando Name Mangling para acessar dados.
# Não fazer esse tipo de acesso

soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas é: {soma}')

'''

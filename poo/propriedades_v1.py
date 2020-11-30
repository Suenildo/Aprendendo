class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property  # Funciona como get ((consulta))
    def numero(self):
        return self.__numero

    @property  # Funciona como get  ((consulta))
    def titular(self):
        return self.__titular

    @property  # Funciona como get  ((consulta))
    def saldo(self):
        return self.__saldo

    @property  # Funciona como get  ((consulta))
    def limite(self):
        return self.__limite

    @limite.setter  # Funciona como set  ((altera))
    def limite(self, novo_limite):
        self.__limite = novo_limite


    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    #  Vamos criar um método com property:
    @property
    def valor_total(self):
        return self.__saldo + self.limite


conta_cliente_01 = Conta('Silvio', 2000, 3000)
conta_cliente_02 = Conta('Silvia', 1000, 5000)

print(conta_cliente_01.extrato())
print(conta_cliente_02.extrato())

soma = conta_cliente_01.saldo + conta_cliente_02.saldo
print(f'A soma do saldo das contas é: {soma}')

print()
# Verificando dados originais:
print(conta_cliente_01.__dict__)
print()

# vamos alterar dados:
conta_cliente_01.limite = 6000

# Verificando dados alterados:
print(conta_cliente_01.__dict__)

print()
print(f'O valor total disponível na conta1 é {conta_cliente_01.valor_total}')
print(f'O valor total disponível na conta2 é {conta_cliente_02.valor_total}')

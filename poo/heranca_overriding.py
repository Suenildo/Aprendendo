"""
Vamos reescrever um métoda da Super Classe
em uma classe filha.
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Aqui  tem (self)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Aqui não tem (self)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # (*)
        return f'Funcionário: {self.__matricula} Nome: {self.nome}'  # Overriding


cliente_1 = Cliente('Juvenal', 'souza', '000.000.111-23', 1000)
funcionario_1 = Funcionario('Nelson', 'pereira', '000.000.122-23', 1234)

print(cliente_1.nome_completo())
print(funcionario_1.nome_completo())

'''
(*) - Com o Super, eu posso acessar o método que eu quiser na Super Classe.
'''

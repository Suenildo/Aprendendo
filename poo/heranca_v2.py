
# Vamos definir uma Super Classe:
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

#  Vamos definir as Classes Filhas:
class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Aqui não tem (self)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Aqui não tem (self)
        self.__matricula = matricula

''' 
super().__init__(nome, sobrenome, cpf) - chama os argumentos 
da classe Mãe. (((((Sem o self))))
Esses agumentos serão utilizados nas classes filhas.
Chama também o método: nome_completo.
'''

# Instanciando objetos:

cliente_1 = Cliente('Juvenal', 'souza', '000.000.111-23', 1000)
funcionario_1 = Funcionario('Nelson', 'pereira', '000.000.111-23', 1234)

print(cliente_1.nome_completo())
print(funcionario_1.nome_completo())

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
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Aqui  tem (self)
        self.__renda = renda


'''
 Se eu chamar a Super classe pelo nome dela, eu tenho que 
usar o (((SELF))), mas não é o método comum de se chamar a Super
Classe, abaixo, na Classe Funcionário, vamos chamar com o modo
correto.
'''


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
funcionario_1 = Funcionario('Nelson', 'pereira', '000.000.122-23', 1234)

print(cliente_1.nome_completo())
print(funcionario_1.nome_completo())

print()

# Vamos chamar os dicionários das Classes filhas:
print(cliente_1.__dict__)
print(funcionario_1.__dict__)

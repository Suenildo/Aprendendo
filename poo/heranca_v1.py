class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


# Instanciando objetos:

cliente_1 = Cliente('Juvenal', 'souza', '000.000.111-23', 1000)
funcionario_1 = Funcionario('Nelson', 'pereira', '000.000.111-23', 1234)

print(cliente_1.nome_completo())
print(funcionario_1.nome_completo())

'''
Podemos notar que há parâmetros e métodos comuns nas duas classes.
Vamos melhor isso em (herança_v2.py)
'''

"""
Atributos são as características de um dado objeto.
Grupos de atributos:
 - Instância --> declarados dentro do método construtor
   - Todo objeto instanciado, vai possuir esses atributos.
   Atributos de Instancia podem ser:
       - Públicos -->  Visível no projeto (default)
       - Privados --> somente visível dentro da sua classe
                      __(nome do atributo): Name Mangling.


 - Classe --> Declarados diretamente na classe, não no construtor,
              geralmente inicializados com um valor, e esse valor é
              é compartilhado entre todas as instâncias.

 - Dinâmico -->
"""


class RevistaQuadrinhos:
    def __init__(self, tipo, titulo):  # Método construtor
        self.tipo = tipo  # atributo de instância (público)
        self.titulo = titulo  # atributo de instância (público)


#  Instanciando um objeto com dois atributos:
revistinha = RevistaQuadrinhos('Heróis', 'Homem Aranha')  # método __init__ sendo executado.

print(revistinha.tipo)
print(revistinha.titulo)


# Como os atributos são públicos o acesso foi concedido.

class Login:
    def __init__(self, senha, user):
        self.__senha = senha  # atributo de instância (privado)
        self.__user = user  # atributo de instância (privado)


usuario = Login('1234', 'nome')

'''Se tentarmos fazer esse acesso:

print(usuario.__user)

ocorrerá o seguinte erro: AttributeError: 'Login' object has no attribute '__user'.

Isso porque (user) é um atributo privado, entretanto, conseguimos fazer o acesso com o 
Name Mangling
'''

print()
print('acessando com Name Mangling')

print(usuario._Login__user)

print()
print('=*=' * 10)


#  Vamos criar uma nova classe com atributo de classe:

class Revistinha:
    padrao = 'colorido'  # atributo de classe

    def __init__(self, tipo, titulo):  # Método construtor
        self.tipo = tipo  # atributo de instância (público)
        self.titulo = titulo  # atributo de instância (público)


revista = Revistinha('Infantil', 'Mônica')
print(revista.padrao)  # Note que na instância eu não citei o padrão.

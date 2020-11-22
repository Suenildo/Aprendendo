"""
Vamos fazer uma função que inverte uma string.
"""


def inverte_string(valor_string):
    resultado = " "
    for caracter in valor_string:
        resultado = caracter + resultado
    return resultado


string = input("Entre com alguma string: ")
while string.strip() != "":
    print("O inverso de ", string, "é ", inverte_string(string))
    string = input("Entre com outra string ou pressione ENTER para sair: ")

"""
Strings podem ser definidos como coleções de sequencias de caracteres.
Isto significa que assumimos que os caracteres individuais que compõem
a cadeia estão em uma determinada ordem, da esquerda para a direita.

Uma cadeia que não possui nenhum caractere, muitas vezes chamada de string
vazio, é também considerado um string. É simplesmente uma sequência com
zero caracteres e é representado por ‘’ ou “”
(dois apóstrofes ou aspas sem nada entre eles – observe que o string com
um ou mais caracteres em branco como ‘ ‘ é diferente do string vazio ‘’).
(https://panda.ime.usp.br/)
"""

texto = 'Eu sou uma string'

# Pegando o tamanho de uma string com "len()":
print('Eu tenho ', len(texto), 'caracteres')

# encontrando a posição de um caracter:
print('Eu estou na posição: ', texto.find('o'))

# Substituindo parte da string:
texto1 = texto.replace('uma', 'da classe')
print(texto1)

# Contando caracteres:
print('A string possui: ', texto1.count('s'), 'caracteres s ')

# Podemos separar uma string:
print(texto.split())
print(texto.split('uma'))  # aqui usei como referencia para separar o "uma"

# *******CONTINUA********
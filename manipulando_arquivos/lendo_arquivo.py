"""
Com o arquivo 'arquivo.txt', no mesmo diretório do código,
vamos fazer algumas operações básica de manipulação.
"""

# Primeiro temos que abrir o arquivo:
arquivo = open("arquivo.txt", "r")

# vamos ler o arquivo:
print(arquivo.read())

# Contando o número de caracteres:
print(arquivo.tell())

# Após a operação realizada, devemos fechar o arquivo.
arquivo.close()

# sequisermos fazer outras operações, devemos abrir novamente o arquivo:
arquivo = open("arquivo.txt", "r")

# Podemos ler os 8 primeiros caracteres (lembre-se: espaço é um caracter):
print(arquivo.read(8))

# Para eu retornar para o início do arquivo:
print(arquivo.seek(0, 0))  # Ele retorna para o início do arquivo
print(arquivo.read())  # O arquivo foi lido por inteiro
arquivo.close()

# Nunca esqueça de fechar o arquivo.
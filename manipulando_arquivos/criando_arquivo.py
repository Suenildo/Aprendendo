"""
Vamos criar o arquivo2.txt
"""
# Usuário dará um nome para o arquivo
nome_arquivo = input("digite um nome para o arquivo: ") # Dado o nome "teste"

# Vamos dar a extensão do arquivo
nome_arquivo = nome_arquivo + '.txt'

# Vamos abrir o arquivo para escrita e inserirmos dados.
arquivo2 = open(nome_arquivo, "w")
arquivo2.write("Inserido esse texto")

# Nunca esquecer de fechar o arquivo.
arquivo2.close()

arquivo2 = open(nome_arquivo, "r")

print(arquivo2.read())

arquivo2.close()


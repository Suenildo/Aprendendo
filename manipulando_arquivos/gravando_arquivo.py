"""
Com o arquivo 'arquivo1.txt', no mesmo diretório do código,
vamos fazer algumas operações básica de manipulação.
"""

# Lembrando de sempre abrir o arquivo.
arquivo = open("arquivo1.txt", "w")

# Vamos gravar no arquivo.
arquivo.write("Arquivo sendo modificado com novo conteúdo")

# Após a modificação desejada, não esquecer de fechar o arquivo.
arquivo.close()

# Vamos ler o arquivo.

# Lembrando de sempre abrir o arquivo.
arquivo = open("arquivo1.txt", "r")

print(arquivo.read())


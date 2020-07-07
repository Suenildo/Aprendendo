"""
Código baseado no curso inicial de PYTHON da
"https://www.datascienceacademy.com.br/"
"""

# Com o arquivo salario.csv no mesmo pacote:

# Vamos colocar o arquivo em uma variável.
arquivo = open('salarios.csv', 'r')

# Vamos criar a variável "dados" para receber a leitura do arquivo.
dados = arquivo.read()

# Vamos fazer com que o arquivo fique em uma linha.
linha = dados.split('\n')  # O método "split" vai retirar a quebra de linha.

print(linha)
arquivo.close()

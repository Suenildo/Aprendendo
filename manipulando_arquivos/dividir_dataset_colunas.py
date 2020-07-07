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
linhas = dados.split('\n')  # O método "split" vai retirar a quebra de linha.

# Vamos criar uma variável tipo "lista" vazia.
todos_dados = []

''' Vamos percorrer toda a linha criada  pegando os dados
    separados por vírgula com um "for" e colocando na "lista'''

for linha in linhas:
    linha_separada = linha.split(',')
    todos_dados.append(linha_separada)

print(todos_dados)

arquivo.close()


"""
Código baseado no curso inicial de PYTHON da
"https://www.datascienceacademy.com.br/"
"""

arquivo = open('salarios.csv', 'r')
dados = arquivo.read()
linhas = dados.split('\n')  # O método "split" vai retirar a quebra de linha.
todos_dados = []

''' Vamos percorrer toda a linha criada  pegando os dados
    separados por vírgula com um "for" e colocando na "lista'''

for linha in linhas:
    linha_separada = linha.split(',')
    todos_dados.append(linha_separada)
    primeira_linha = todos_dados[0]

contador = 0

for coluna in primeira_linha:
    contador += 1

'''   OU

    for coluna in todos_dados[0]:
        contador += 1
'''

print(contador)

arquivo.close()

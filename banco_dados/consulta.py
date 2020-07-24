import random
import sqlite3

conexao = sqlite3.connect('novo3.db')
crs = conexao.cursor()


def criador_tabela():
    crs.execute("create table if not exists brinquedos ("
                "id interger primary key  not null,"
                " nome text,"
                " tipo text,"
                " preço REAL)")
    conexao.commit()


def inserir_com_variaveis():
    novo_id = random.randrange(1, 1000)  # (*)
    novo_nome = 'bola'
    novo_tipo = 'futebol'
    novo_preco = random.randrange(10, 60)
    crs.execute("insert into brinquedos(id, nome, tipo, preço) values(?, ?, ?, ?)",
                (novo_id, novo_nome, novo_tipo, novo_preco))
    conexao.commit()


criador_tabela()

for n in range(5):
    inserir_com_variaveis()

# Vamos fazer  pesquisas no BD usando Python:
def lendo_dados():
    crs.execute("select * from brinquedos")
    for linhas in crs.fetchall():
        print(linhas)

def lendo_uma_coluna():
    crs.execute("select * from brinquedos")
    for linha in crs.fetchall():
        print(linha[3])


lendo_dados()
lendo_uma_coluna()
crs.close()
conexao.close()

# (*) Foi pego um intervalo grande para não haver repetição.

''' Caso você vá executar o programa mais de uma vez, 
lembre-se de sempre apagar o banco de dados antes de executar, 
porque senão, vai dar erro'''

import random
import sqlite3
import matplotlib.pyplot as plt

conexao = sqlite3.connect('novo4.db')
crs = conexao.cursor()


def criador_tabela():
    crs.execute("create table if not exists brinquedos ("
                "id interger primary key  not null,"
                " nome text,"
                " tipo text,"
                " preco REAL)")
    conexao.commit()


def inserir_com_variaveis():
    novo_id = random.randrange(1, 1000)
    novo_nome = 'bola'
    novo_tipo = 'futebol'
    novo_preco = random.randrange(10, 60)
    crs.execute("insert into brinquedos(id, nome, tipo, preco) values(?, ?, ?, ?)",
                (novo_id, novo_nome, novo_tipo, novo_preco))
    conexao.commit()


criador_tabela()

for n in range(5):
    inserir_com_variaveis()


def cria_grafico():
    crs.execute("select tipo, preco from brinquedos")
    tipo = []
    preco = []
    dados = crs.fetchall()
    for linha in dados:
        tipo.append(linha[0])
        preco.append(linha[1])

    plt.bar(tipo, preco)
    plt.show()

cria_grafico()
crs.close()
conexao.close()

# (*) Foi pego um intervalo grande para não haver repetição.

''' Caso você vá executar o programa mais de uma vez, 
lembre-se de sempre apagar o banco de dados antes de executar, 
porque senão, vai dar erro'''
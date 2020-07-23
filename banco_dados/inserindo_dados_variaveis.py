import random
import sqlite3

# Criando uma conexão,  salvando no objeto "conexao"
# Se o banco de dados não existir, ele é criado neste momento.


conexao = sqlite3.connect('novo2.db')

crs = conexao.cursor()


# VAmos criar uma função que cria tabelas:
def criador_tabela():
    crs.execute("create table if not exists brinquedos ("
                "id interger primary key  not null,"
                " nome text,"
                " tipo text,"
                " preço REAL)")
    conexao.commit()
# para gerar id autmático, use o AUTOINCREMENT.

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

crs.close()
conexao.close()

# (*) Foi pego um intervalo grande para não haver repetição.

''' Caso você vá executar o programa mais de uma vez, 
lembre-se de sempre apagar o banco de dados antes de executar, 
porque senão, vai dar erro'''
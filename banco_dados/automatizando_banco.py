import sqlite3

# Criando uma conexão,  salvando no objeto "conexao"
# Se o banco de dados não existir, ele é criado neste momento.

# -----inicio do bloco para automatizar--------
conexao = sqlite3.connect('novo.db')

crs = conexao.cursor()


# VAmos criar uma função que cria tabelas:
def criador_tabela():
    crs.execute("create table if not exists brinquedos ("
                "id interger primary key  not null,"
                " nome text,"
                " tipo text,"
                " preço REAL)")
    conexao.commit()


# Vamos criar uma fução que insere dados (linha)
def insere_dados():
    crs.execute("insert into brinquedos values(10, 'bola', 'esporte', 20)")
    conexao.commit()
    crs.close()
    conexao.close()


# -----Fim do bloco para automatizar--------

criador_tabela()

insere_dados()

''' Caso você vá executar o programa mais de uma vez, 
lembre-se de sempre apagar o banco de dados antes de executar, 
porque senão, vai dar erro'''
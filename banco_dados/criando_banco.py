# Vamos importar o módulo da linguagem Python que nos permite acessar o SQLite
import sqlite3

# Criando uma conexão,  salvando no objeto "conexao"
# Se o banco de dados não existir, ele é criado neste momento.
conexao = sqlite3.connect('corona.db')

'''
Criando um cursor

Em ciência da computação, um cursor de banco de dados é uma estrutura
de controle que permite percorrer sobre os registros em um banco de dados.
Os cursores facilitam o processamento subsequente em conjunto com o
percorrimento, tal como recuperação, adição e remoção de registros de
banco de dados.  
               (pt.wikipedia.org › wiki › Cursor_(banco_de_dados))

Um cursor permite percorrer todos os registros em um conjunto de dados
O cursor lhe dá acesso ao banco de dados

'''

crs = conexao.cursor()

# Vamos criar nossa primeira tabela no banco de Dados (DDL)
cria_tabela = 'create table if not exists dados ' \
              '(id integer primary key,' \
              'País varchar(100), ' \
              'Casos integer)'

'''
Vamos chamar a função ".execute" do meu objeto crs (meu cursor),
passando como parâmetro minha variável "cria_tabela" '''
crs.execute(cria_tabela)

# Vamos criar uma variável para inserção de dados
insere_dados = 'insert into dados values (?, ?, ?)'

insercao = [(1, 'Brasil', '10000'),
            (2, 'Italia', '21000'),
            (3, 'USA', '30000')]

# Vamos criar um laço "for" para percorrer e inserir os dados
for registros in insercao:
    crs.execute(insere_dados, registros)

'''Vamos executar o commit, para o que foi criado, ser gravado
no banco de dados. O commit é chamado com a conexão do BD'''
conexao.commit()

# Vamos fazer uma consulta ao banco de dados criado

# Vamos criar um objeto para pesquisa:
pesquisa_1 = 'select * from dados'

# Vamos executar o objeto criado com o "execute".
# Vamos criar um objeto para salvar os registros pesquisados.
crs.execute(pesquisa_1)
pesquisado = crs.fetchall()

# Através de um "for", vamos listar o conteúdo de "pesquisado"
for linha in pesquisado:
    print('Id: %d, País: %s, Casos: %d \n' % linha)




'''
cursor.fetchall() fetches all the rows of a query result. 
It returns all the rows as a list of tuples. An empty list
 is returned if there is no record to fetch.

cursor.fetchmany(size) returns the number of rows specified 
by size argument. When called repeatedly this method fetches 
the next set of rows of a query result and returns a list of 
tuples. If no more rows are available, it returns an empty list.

cursor.fetchone() method returns a single record or None if no more
rows are available.
'''

# Importante: não esqueça de fechar a conexão.
conexao.close()

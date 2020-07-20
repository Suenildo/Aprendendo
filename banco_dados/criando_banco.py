
import sqlite3
# sqlite é nativa no python


# Criando uma conexão
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

# Vamos criar nossa primeira tabela no banco de Dados
cria_tabela = 'create table dados ' \
              '(id integer primary key,' \
              'País varchar(100), ' \
              'Casos varchar(100))'

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
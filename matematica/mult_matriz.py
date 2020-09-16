"""
Algorítimo básico para multiplicar matrizes,
sem utilizar o numpy.
"""


def multiplica_matriz(A, B):
    """
    Função para multiplicar matrizes
    :param x: Matriz 1
    :param y: Matriz 2
    :return: Matriz resultante do produto 1 por 2
    """
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])

    if colunas_A != linhas_B:
        print('Não será possível multiplicar as matrizes dadas,'
              'Dimensões incorretas')
        return

    C = [[0 for linha in range(colunas_B)] for coluna in range(linhas_A)]
    print(f'Matriz C = {C}')

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


x = [[1, 2, 3, 4], [2, 4, 5, 8]]
y = [[1, 6], [5, 3], [1, 2], [1, 4]]

C = multiplica_matriz(x, y)
print(f'O resultado de A x B é  C = {C}')

print()

print('Entendendo o que são os ranges nos loops aninhados:')
print(f' Eu sou linhas_A --> {len(x)}')
print(f' Eu sou colunas_B --> {len(y[0])}')
print(f' Eu sou linhas_B --> {len(y)}')
print(f' Eu sou colunas_A --> {len(x[0])}')
'''
linha 14:
Obtenho quantas linhas eu tenho, como estamos usando listas, 
leva-se em consideração que cada linha, é um elemento da lista.
Ex:
a =  [ [1, 2, 3],   [4, 6, 7],   [8, 7, 9]]
    | elemento 0    elemento 1   elemento 2 | = tamanho = 3 
Teremos 3 linhas, len = 3

linha 15:
Obtenho quantas colunas existem, ou seja, quantos elementos
eu tenho dentro do primeiro elemento.
Ex:
a =  [ [1, 2, 3],   [4, 6, 7],   [8, 7, 9]]
    | elemento 0    elemento 1   elemento 2 | 
| elemento 0 | = [1, 2, 3] = 3 elementos = 3 colunas 
Teremos 3 colunas

As linhas 16 e 17 seguem o mesmo raciocínio. 

linha 19:
Condiciona a operação de multiplicação de Matrizes de acordo com a regra;
O número de colunas da Matriz A, 
tem que ser igual ao número de linhas da Matriz B.
Se a condição for verdadeira, o programa acaba ali.

linha 24:
Vamos criar uma Matriz C que, a princípio terá todos os valores
iguais a zero e de ordem:
Número de linhas de A e número de colunas de B.
[ 0 for linha in range(colunas_B)]   for   coluna in range(linhas_A)]
| preencherá as linhas com zeros |   | preencherá as colunas com zeros |

linha 25:
Será printada a Matriz C somente para verificação.

linha 27:
for i in range(linhas_A): percorrerá todas as linhas da Matriz A

linha 28:
for j in range(colunas_B): percorrerá todas as colunas da Matriz B

linha 29:
for k in range(colunas_A): percorrerá todas as colunas da Matriz A

linha 30:
 C[i][j] += A[i][k] * B[k][j], vejamos quem é cada elemento:
 C[i = 0][j = 0]:
  - na Matriz C esse elemento começa com 0;
 A[i = 0][k = 0]:
  -  primeira linha, primeira coluna = 1
 B[k = 0][j = 0]:
  - K = 0 pois está no range das colunas de A que é 2:
    - [[1, 2, 3, 4], [2, 4, 5, 8]]
          k = 0         k = 1     range  = 2
  - j = 0
  ou seja, esse elemento é = 1
  [   [1,     6],     [5, 3],     [1, 2],     [1, 4] ]
    k=0, j=0
    
Então :
C[i][j] += A[i][k] * B[k][j] com: i, j, k = 0 , teremos:
0 + 1 * 1 = 1 que é o primeiro elemento da Matriz C.
Os demais elementos são intuitivos, seguindo esse padrão.
'''

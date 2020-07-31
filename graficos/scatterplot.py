"""
scatterplot = gráfico de dispersão.
Os diagramas de dispersão ou gráficos de dispersão são representações
de dados de duas ou mais variáveis que são organizadas em um gráfico.
O gráfico de dispersão utiliza coordenadas cartesianas para exibir
valores de um conjunto de dados.
Wikipédia
"""


from matplotlib import pyplot as plt

x = [2, 8, 6, 7,10, 9]
y = [7, 9, 12, 10, 8, 6]

plt.scatter(x, y, label = 'Pontos', color = 'y', marker = '*', s = 80)
plt.legend()
plt.show()

'''
plt.scatter(x, y, label = 'Pontos', color = 'y', marker = '*', s = 80)
- label = 'Pontos' : (nome da legenda)
- color = 'y' : cor dos marcadores (pontos)
- marker = '*' : estilo do marcador
- s = 80 : tamanho do marcador
'''

x1 = [2, 8, 6, 7, 10, 9, 11, 15, 20, 1, 18]
y1 = [7, 9, 12, 10, 8, 6, 16, 7, 15, 13, 11]

plt.scatter(x1, y1, label = 'Pontos', color = 'r', marker = 'o', s = 300)
plt.legend()
plt.show()


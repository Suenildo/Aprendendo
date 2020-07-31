"""
O gráfico de barras é um gráfico com barras retangulares e comprimento
proporcional aos valores que ele apresenta.
Este tipo de representação utiliza barras tanto verticais quanto horizontais
para ilustrar comparações (sendo o primeiro mais conhecido como gráfico de colunas).
https://pt.wikipedia.org
"""
from matplotlib import pyplot as plt

x = [1, 5, 3, 10, 2]
y = [3, 25, 9, 5, 4]

plt.bar(x, y, label='relação', color="b")  # adicionando legenda e cor das barras
plt.xlabel('número')  # adicionando nome ao eixo x
plt.ylabel('quadrado do número')  # adicionando nome ao eixo y
plt.title('Relação número/quadrado')  # adicionando título ao gráfico
plt.legend()
plt.show()

x1 = [2, 6, 6, 12, 7]
y1 = [5, 9, 4, 3, 8]

plt.bar(x, y, label='notação 1', color="b")
plt.bar(x1, y1, label='notação 2', color="r")
plt.legend()
plt.show()

# Exemplo usando List comprehension:
quantidades = [40, 50, 35, 25, 19, 63, 39, 10]
produtos = [quant for quant in range(len(quantidades))]
# Para cada quantidade em um range do tamanho de quantidades,
# eu armazeno produtos.

plt.bar(produtos, quantidades)
plt.show()


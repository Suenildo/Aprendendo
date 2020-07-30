"""
Para criação de gráficos, vamos utilizat  o matplotlib, caso você não
o tenha instalado, use o pip para instalá-lo.
"""



from matplotlib import pyplot as plt

# Vamos fazer um plot simples
plt.plot([2, 4, 6], [4, 16, 36])
plt.show()                                # comando para mostrar o plot

# Agora vamos usar variáveis:
x = [1, 3, 5, 7]
y = [1, 9, 25, 49]

# Vamos inserir dados no gráfico:
plt.plot(x, y, label = 'relação')           # adicionando legenda
plt.xlabel('número')                        # adicionando nome ao eixo x
plt.ylabel('quadrado do número')            # adicionando nome ao eixo y
plt.title('Relação número/quadrado')        # adicionando título ao gráfico
plt.legend()
plt.show()
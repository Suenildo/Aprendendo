"""
como usar if, elif & else em uma função lambda.

sintaxe:
lambda <args> : <return Value> if <condition > ( <return value > if <condition> else <return value>)
"""

checa = lambda x: False if (x > 6 and x < 12) else True
print(checa(7))
print(checa(3))
print(checa(20))


verifica = lambda x: x * 2 if x < 5 else (x * 3 if x < 8 else x)
print(verifica(4))
print(verifica(6))
print(verifica(9))

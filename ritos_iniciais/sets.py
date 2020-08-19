"""
Os sets são uma coleção de itens desordenada, parcialmente
imutável e que não podem conter elementos duplicados.
Por ser parcialmente imutável, os sets possuem permissão
das operações de  adição e remoção de elementos.
"""

# Vamos declarar um set:
set_01 = {2, 4, 6, 8}
print(type(set_01))

set_02 = set([1, 2, 8, 9, 10])
print(type(set_02))


# Adicionando elementos
set_01.add(10)
print("Adição", set_01)

# Atualizando set
set_01.update([3, 6, 9, 12])
print("Atualição", set_01)

# Removendo elemento
set_01.discard(12)
print("Remoção", set_01)


set_03 = {1, 2, 3, 4, 1}
set_04 = {1, 2, 8, 9, 10}

# União
print("União")
print(set_03 | set_04)
print(set_03.union(set_04))

# Interseção
print("Interseção")
print(set_03 & set_04)
print(set_03.intersection(set_04))

# Diferença
print("Diferença")
print(set_03 - set_04)
print(set_03.difference(set_04))

# Diferença Simétrica
print("Diferença Simétrica")
print(set_03 ^ set_04)
print(set_03.symmetric_difference(set_04))
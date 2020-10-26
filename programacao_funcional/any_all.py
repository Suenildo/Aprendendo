"""
all - Retorna verdadeiro se todos os elementos do iterável
são verdadeiros ou está vazio.

any -
"""

print('Exemplos:')

a = [1, 5, 8, 3, 0, 4, 7]
b = (1, 2, 5, 8, 14, 18, 20)
c = {}
frutas = ['maçã', 'mamão', 'manga', 'mangaba', 'uva']
verifica = all([frutas[0] == 'm' for nome in frutas])

print(f' eu sou {all(a)} por causa do 0')
print(f' Eu sou {all(b)}')
print(f' Eu sou {all(c)} porque sou vazio')
print(f'Sou {verifica}, porque uva não começa com m.')



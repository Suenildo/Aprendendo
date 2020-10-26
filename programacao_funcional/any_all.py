"""
all - Retorna verdadeiro se todos os elementos do iterável
são verdadeiros ou está vazio.

any - Retorna verdadeiro se qualquer elemento do iterável
for verdadeiro, e, se o iterávivel for vazio, ela retorna falso.
"""

print('Exemplos: all()')

a = [1, 5, 8, 3, 0, 4, 7]
b = (1, 2, 5, 8, 14, 18, 20)
c = {}
frutas = ['maçã', 'mamão', 'manga', 'mangaba', 'uva']
verifica = all([frutas[0] == 'm' for nome in frutas])
multiplos_tres = [15, 9, 21, 45, 6, 90]
verifica_1 = all([num for num in multiplos_tres if num % 3 == 0])

print(f'Eu sou {all(a)} por causa do 0')
print(f'Eu sou {all(b)}')
print(f'Eu sou {all(c)} porque sou vazio')
print(f'Sou {verifica}, porque uva não começa com m.')
print(f'Sou {verifica_1}, porque só possuo múltplos de três')

print('Outras maneiras de utilização:')
# Código do aluno Renato do curso:
# Python do básico ao avançado na Udemy.
print(all([False for letra in 'a' if letra not in 'aeiou']))

print(all([False for num in [2, 4, 6, 8, 10, 12, 13] if num % 2]))

'''
Tomar cuidado com essa função, pois se você fizer retornar 
um iterável vazio, ele retornará True
'''

print()
print()
print('Exemplos: any()')

frutas_1 = ['maçã', 'mamão', 'manga', 'mangaba']
verifica_2 = any([frutas_1[0][0] == 'm' for nom in frutas_1])
verifica_3 = any([num for num in multiplos_tres if num % 3 == 0])

print(f'Eu sou {any(a)} porque tem pelo menos um elemento verdadeiro')
print(f'Eu sou {any(b)}')
print(f'Eu sou {any(c)} porque sou vazio')
print(f'Sou {verifica_2}, porque pelo menos uma palavra começa com m.')
print(f'Sou {verifica_3}, porque só possuo múltplos de três')



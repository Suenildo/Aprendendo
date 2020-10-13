"""
Usando o While para corrigir provas
"""

acertos = 0
pergunta = 1

while pergunta <= 5:
    resposta = str(input(f' A resposta da questão {pergunta} é: '))
    if pergunta == 1 and resposta == 'a':
        acertos += 1
    if pergunta == 2 and resposta == 'c':
        acertos += 1
    if pergunta == 3 and resposta == 'd':
        acertos += 1
    if pergunta == 4 and resposta == 'b':
        acertos += 1
    if pergunta == 5 and resposta == 'a':
        acertos += 1
    pergunta +=1

print(f'O candidato teve {acertos} acertos ')
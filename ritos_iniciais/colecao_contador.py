"""
Counter é uma subclasse dicionário para contar objetos.
É uma coleção em que os elementos são armazenados como
chaves do dicionário e suas contagens são armazenadas como
valores do dicionário. É permitido que contagens sejam
qualquer valor inteiro, incluindo contagens zero ou negativas.
"""

from collections import Counter

print('Retirado da Documentação do Python')
a = Counter()  # a new, empty counter
b = Counter('gallahad')  # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
d = Counter(cats=4, dogs=8)  # a new counter from keyword args

print(a)
print(b)
print(c)
print(d)

print()

print('=*=' * 25)

print('Exemplos:')
# Será exibido um dicionário com as repetições de cada caracter inclusive o espaço
frase = 'Aqui serão contadas todas as repeticoes de letras e os espacos'
contador = Counter(frase)
print(contador)

print()

frase1 = '''Aqui serão contadas as repetições das palavras que estão
nesta frase, serão contadas uma por uma'''
palavra = frase1.split()
res = Counter(palavra)
print(res)

print()
print('=*=' * 25)
# Vamos pegar um texto maior

texto = """1.Toda a sabedoria vem do Senhor Deus, ela sempre esteve com ele. 
Ela existe antes de todos os séculos. 2.Quem pode contar os grãos de areia do mar, as 
gotas de chuva, os dias do tempo? Quem pode medir a altura do céu, a extensão da 
terra, a profundidade do abismo? 3.Quem pode penetrar a sabedoria divina, anterior a 
tudo? 4.A sabedoria foi criada antes de todas as coisas, a inteligência prudente 
existe antes dos séculos! 5.O Verbo de Deus nos céus é fonte de sabedoria, seus 
caminhos são os mandamentos eternos. 6.A quem foi revelada a raiz da sabedoria? 
Quem pode discernir os seus artifícios? 7.A quem foi mostrada e revelada a 
ciência da sabedoria? Quem pode compreender a multiplicidade de seus caminhos? 
8.Somente o Altíssimo, criador onipotente, rei poderoso e infinitamente temível, 
Deus dominador, sentado no seu trono; 9.foi ele quem a criou no Espírito Santo, 
quem a viu, numerada e medida;* 10.ele a aspergiu em todas as suas obras, sobre 
toda a carne, à medida que a repartiu, e deu-a àqueles que a amavam. 11.O temor 
do Senhor é uma glória, um motivo de glória, uma fonte de alegria, uma coroa 
de regozijo. 12.O temor do Senhor alegra o coração. Ele nos dá alegria, regozijo 
e longa vida. 13.Quem teme o Senhor se sentirá bem no instante derradeiro, no 
dia da morte será abençoado. 14.O amor de Deus é uma sabedoria digna de ser 
honrada. 15.Aqueles a quem ela se mostra amam-na logo que a veem, logo que 
reconhecem os prodígios que realiza. 16.O temor do Senhor é o início da sabedoria. 
Ela foi criada com os homens fiéis no seio de sua mãe, ela caminha com as mulheres 
de escol, vemo-la na companhia dos justos e dos fiéis. 17.O temor do Senhor é a 
religião da ciência.* 18.Essa religião guarda e santifica o coração; ela lhe traz 
satisfação e alegria. 19.Aquele que teme ao Senhor será confortado, no dia da 
morte será abençoado. 20.O temor do Senhor é a plenitude da sabedoria, a plenitude 
de seus frutos, para aquele que a possui 21.ela enche toda a sua casa com os bens 
que produz, e seus celeiros com seus tesouros. 22.O temor do Senhor é a coroa da 
sabedoria: dá uma plenitude de paz e de frutos de salvação. 23.Ele a viu e 
numerou-a; ora, um e outra são um dom de Deus. 24.A sabedoria distribui a 
ciência e a prudente inteligência; eleva à glória aqueles que a possuem. 
25.O temor do Senhor é a raiz da sabedoria, seus ramos são de longa duração. 
26.A inteligência e a religião da ciência se acham nos tesouros da sabedoria, 
mas a sabedoria é abominada pelos pecadores. 27.O temor do Senhor expulsa o 
pecado, 28.pois aquele que não tem esse temor não poderá tornar-se justo. 
A violência de sua paixão causará sua ruína. 29.O homem paciente esperará 
até um determinado tempo, após o qual a alegria lhe será restituída. 30.O 
homem de bom senso guarda suas palavras; muitos falarão, em voz alta, de 
sua prudência. 31.O sentido da instrução está encerrado nos celeiros da 
sabedoria. 32.Mas o culto de Deus é abominado pelo pecador. 33.Meu filho, 
tu que desejas ardentemente a sabedoria, sê justo e Deus te concederá. 
34.Pois o temor do Senhor é sabedoria e instrução, e o que lhe é agradável 
35.é fidelidade e doçura; ele encherá os celeiros daqueles (que as possuem). 
36.Não sejas rebelde ao temor do Senhor, não vás a ele com um coração fingido. 
37.Não sejas hipócrita diante dos homens, e que teus lábios não sejam motivo de 
queda. 38.Vela sobre eles para que não caias, e não atraias sobre tua alma a 
desonra; 39.e para que Deus, revelando teus segredos, não te destrua no meio da 
assembleia, 40.por te teres aproximado do Senhor sorrateiramente, com o coração 
cheio de astúcia e engano."""

palavras = texto.split()
cont_palavras = Counter(palavras)
print(cont_palavras)
print()
print('As dez palavras que mais aparecem no texto, são:')
print(cont_palavras.most_common(12))



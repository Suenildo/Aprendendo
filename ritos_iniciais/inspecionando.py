import sys
import keyword

c = ('\033[m',             # sem cor
     '\033[0;30;41m',      # vermelho
     '\033[0;30;42m',      # verde
     '\033[0;30;43m',      # amarelo
     '\033[0;30;44m',      # azul
     '\033[0;30;45m',      # roxo
     '\033[7;30m')         # branco


print(c[6],'Versão do Python :', sys.version, c[0])
print()
print(c[2],'Localização do interpretador: ', sys.executable, c[0])
print()
print(c[1],'Palavras chaves', c[0])
for palavra in keyword.kwlist:
    print(palavra)

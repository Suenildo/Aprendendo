"""
re.compile(padrão, string)
Podemos combinar uma expressão regular com objetos de padrões,
que pode ser usado para encontrar padrões. É útil também para
buscar um padrão sem ter que re-escrevê-lo
"""
import re

padrao = re.compile('BR')
resultado = padrao.findall('BR é a sigra do Brasil')
print(resultado)

novo_resultado = padrao.findall('BR tem um significado de Brasi,'
                                ' exemplo: 55 é BR.'
                                'Temos as Rodovias BR também')
print(novo_resultado)
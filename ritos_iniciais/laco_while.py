"""
O loop while executa um conjunto de instruções enquanto uma condição
é verdadeira. Quando essa condição passa a ser falsa, o loop é interrompida.
"""
count = 0
while count <= 5:
    print(count)
    count += 1

print()

# Podemos usar o "else" com o while, como foi usado no "for".
i = 2
while i < 6:
    print(i)
    i += 1
else:
    print("Acabou o while")


"""
Esse código deve rodar até que a palavra "sair" seja digitada.
* Caso uma palavra com 2 ou menos caracteres seja digitada, um aviso
  deve ser exibido e o loop será executado do início (devido ao
  continue), pedindo uma nova palavra ao usuário.
* Caso qualquer outra palavra diferente de "sair" seja digitada, um
  aviso deve ser exibido.
* Por fim, caso a palavra seja "sair", uma mensagem deve ser exibida e o
  loop deve ser encerrado (break).
"""
while True:
    string_digitada = input("Digite uma palavra: ")
    if string_digitada.lower() == "sair":
        print("Fim!")
        break
    if len(string_digitada) < 2:
        print("String muito pequena")
        continue
    print('Tente digitar "sair" ')

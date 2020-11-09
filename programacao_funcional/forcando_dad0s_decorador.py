"""
Exercício retirado do curso:
Programação em python do Básico ao Avnçado.
Geek University, "Evolua seu lado geek.
Plataforma: Udemy
Curso muito bom, recomendo com emprenho.


Forçando tipos de dados com decoradores
"""


def forca_tipos(*tipos):
    def decorador(fun):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return fun(*novo_args, **kwargs)

        return converte

    return decorador


@forca_tipos(str, int)
def repete_msg(msg, vezes):
    for veze in range(vezes):
        print(msg)


repete_msg("Geek", 3)  # Imprimie a String 3 Vezes


@forca_tipos(float, float)
def dividir(a, b):
    print(a / b)


dividir("20", '10')

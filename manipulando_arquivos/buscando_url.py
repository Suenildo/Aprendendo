"""
Vamos fazer uma função que busca uma URL através da biblioteca:
"requests"
Código aprendido no curso:
- Python Pro
_ https://www.python.pro.br/
Excelente cuso, indico com empenho.
"""
import requests


def busca_avatar(usuario):
    """
    Busca o avatar de um usuário no Github
    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(busca_avatar('michael'))

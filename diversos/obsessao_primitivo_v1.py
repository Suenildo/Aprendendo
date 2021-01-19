from typing import NamedTuple, Dict


class Pessoa(NamedTuple):
    nome: str
    sobrenome: str
    telefone: Dict[str, str]
    ddd: int


paulo = Pessoa( 'Paulo',  ' madeira', { 'residencial': '1111-1111', 'movel': '9999-9999'}, 99)

print(paulo)

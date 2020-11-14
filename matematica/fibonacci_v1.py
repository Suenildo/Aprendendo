"""
Com essa função, nós podermos escolher um determinado
ponto da sequência de fibonacci.
Por exemplo:

Qual o número que ocupa a posição 6 e 25 na sequência de fibonacci?
"""

def fibonacci(n: int):
    if n == 0:
        return n
    anterior: int = 0
    posterior: int = 1
    for _ in range(1, n):
        anterior, posterior = posterior, anterior + posterior
    return posterior


if __name__ == '__main__':
    print(fibonacci(6))
    print(fibonacci(50))

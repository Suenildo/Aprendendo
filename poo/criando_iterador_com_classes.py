class Iterador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


for i in Iterador(1, 61):
    print(i, end=" ")

print()

for j in range(1, 61):
    print(j, end=" ")

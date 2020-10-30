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


for i in Iterador(0, 11):
    print(i, end=" ")

print()

for j in range(0, 11):
    print(j, end=" ")

class Carro():
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def __str__(self):
            return "Carro [cor: %s, modelo: %s, ano: %s]" % (self.cor, self.modelo, self.ano)


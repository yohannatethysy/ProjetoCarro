from Carro import Carro
from Hibrido import Hibrido

def main():
    a1 = Carro("Verde laguna", "Palio Fire", "2007")
    a2 = Hibrido("Branco", "Ford Fusion", "2010")

    a1.acelerar()
    a1.frear()
    print(a1)

    a2.acelerar()
    a2.frear()
    a2.carregarBateria()
    print(a2)

if __name__ == '__main__':
    main()




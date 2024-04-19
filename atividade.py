class Veículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        return(f"{self.marca} {self.modelo} o veículo está freando.")

    def acelerar(self):
        return (f"{self.marca} {self.modelo} o veículo está acelerando.")

class Carro(Veículo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    def abrir_porta(self):
        return (f"as portas do {self.marca} {self.modelo} {self.cor} estão abertas")

class Moto(Veículo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def empinar(self):
        return (f"{self.marca} {self.modelo} {self.cilindrada} está empinando")

if __name__ == "__main__":
    carro = Carro ("Porshe", "Porshe 911", "cinza")      
    print(carro.frear())
    print(carro.acelerar())
    print(carro.abrir_porta())

    moto = Moto ("kawazaki", "kawazaki Z1000", "1000cc")
    print(moto.empinar())
    print(moto.acelerar())


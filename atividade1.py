#alunas: Ana Vitoria Cavalcante e Elisa Gomes 3ºA
class Carro:
    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor

    def ligar (self):
        return f'{self.modelo} está ligado'
    def desligar(self):
        return f'{self.modelo} está desligado'
    def acelerar (self):
        return f'{self.modelo} está acelerando'
    
if __name__ == "__main__":
    carro1 = Carro ("toyota", "corolla", "2020", "cinza")
    print(carro1.ligar())
    print(carro1.acelerar())
    print(carro1.desligar())

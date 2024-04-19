#alunas: Ana Vitória Cavalcante e Elisa Gomes 3º A
class Animal: 
    def __init__ (self, nome, idade, espécie):
        self.nome = nome
        self.idade = idade
        self.espécie = espécie 

    def som (self): 
        return f'{self.nome} está emitindo um som: miau miau'
    def informacoes (self): 
        return f'{self.nome}, {self.idade}, {self.espécie}, são as informações do {self.nome}'
    
if __name__ == "__main__":
     animal1= Animal ("mingau", "3 meses", "gato")
     print(animal1.som())
     print(animal1.informacoes())
    
    
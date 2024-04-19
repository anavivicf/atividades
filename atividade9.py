class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    def calcular_media(self):
        total = 0
        for nota in self.notas:
            total += nota
        return total / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        return f"{self.nome} {'foi aprovado' if media >= 6 else 'foi reprovado'} com média {media:.2f}."

if __name__ == "__main__":
    aluno1 = Estudante("Livia", 15, [7, 5, 10, 9])
    aluno2 = Estudante("Lucas", 16, [8, 6, 9, 7])
    
    print(aluno1.verificar_aprovacao())
    print(aluno2.verificar_aprovacao())

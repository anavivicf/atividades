class Livro: 
    def __init__ (self, título, autor, número_de_páginas):
        self.título = título
        self.autor = autor
        self.número_de_páginas = número_de_páginas

    def informacoes (self): 
        return f'{self.título}, {self.autor}, {self.número_de_páginas} páginas, são as informações de {self.título}'

    def total_palavras(self): 
        if self.número_de_páginas == 0:
            return 0
        else:
            return self.número_de_páginas * 250

if __name__ == "__main__":
    livro1 = Livro("Felicidade Clandestina", "Clarice Lispector", 2)
    print(livro1.informacoes())
    print("Total de palavras:", livro1.total_palavras())

class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0.0
        self.status = "Pendente"
    
    def adicionar_item(self, item, quantidade, preco):
        self.itens.append((item, quantidade, preco))
        self.total += quantidade * preco

    def calcular_total(self):
        return sum(quantidade * preco for _, quantidade, preco in self.itens)

    def alterar_status(self, novo_status):
        self.status = novo_status

if __name__ == "__main__":
    pedido1 = Pedido()
    pedido1.adicionar_item("pizza", 1, 20.0)
    pedido1.adicionar_item("refrigerante", 1, 7.0)
    print("Itens do pedido:", pedido1.itens)
    print("Total a ser pago:", pedido1.calcular_total())
    pedido1.alterar_status("Concluído")
    print("Status do pedido:", pedido1.status)

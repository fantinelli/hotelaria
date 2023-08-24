class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.quartos:
            if quarto.esta_disponivel():
                quartos_disponiveis.append(quarto)
        return quartos_disponiveis


class Quartos:
    def __init__(self, numero, capacidade, preco):
        self.numero = numero
        self.capacidade = capacidade
        self.preco = preco
        self.esta_reservado = False

    def esta_disponivel(self):
        return not self.esta_reservado

    def obter_detalhes_quarto(self):
        return f"Quarto {self.numero} - Capacidade: {self.capacidade} pessoas, Preço: {self.preco} por noite"


class ApartamentoSimples(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=1, preco=150) 
# o "super()" que nós utilizamos é para acessar os métodos e atributos da classe pai "Quartos" em uma hierarquia

class ApartamentoSimplesCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=180)


class ApartamentoDuplo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=200)

class ApartamentoDuploCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=220)


class ApartamentoLuxo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=300)


class ApartamentoMaster(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=400)


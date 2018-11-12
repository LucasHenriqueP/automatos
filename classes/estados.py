class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.transicao = []
        pass

    def addTransicao(self, transicao):
        self.transicao.append(transicao)

    def getNome(self):
        return self.nome

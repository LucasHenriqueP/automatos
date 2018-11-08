class Estado:
    def __init__(self, nome):
        self.c = nome
        self.transicao = []
        pass

    def addTransicao(self, transicao):
        self.transicao.append(transicao)

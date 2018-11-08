class Estado:
    def init(self, nome):
        self.nome = nome
        self.transicao = []
        pass

    def addTransicao(self, transicao):
        self.transicao.append(transicao)    
class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.trans = list()

    def getNome(self):
        return self.nome

    def addTransicao(self, trans):
        self.trans.append(trans)

class Transicao:
    def __init__(self, dado, escrever, direcao, nextState):
        self.dado = dado
        self.escrever = escrever
        self.direcao = direcao
        self.nextState = nextState

    def __str__(self):
        return("Se o conteudo for (%s) vou para o estado (%s), a fita vai ter escrito (%c) e vai para a direcao (%s)" % (self.dado, self.nextState, self.escrever, self.direcao))

    def getDado(self):
        return self.dado
    def getEscrever(self):
        return self.escrever
    def getDirecao(self):
        return self.direcao
    def getNextState(self):
        return self.nextState        

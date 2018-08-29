class SuperControle:
    def __init__(self):
        self.controles = list()
        self.atual = 0

    def addControle(self, controle):
        self.controles.append(controle)

    def addAtual(self):
            self.atual = self.atual+1

    def getAtual(self):
        return self.atual

    def getControle(self):
        return self.controles[self.atual]
class Controle:
    def __init__(self, inicio, estados, fim, fita):
        self.inicio = inicio
        self.estados = estados
        self.fim = fim
        self.fita = fita

    def addEstado(self, estado):
        self.estados.append(estado)

    def addFim(self, fim):
        self.fim.append(fim)

    def getInicio(self):
        for i in range(len(self.estados)):
            if self.estados[i].getNome() == str(self.inicio):
               # print("ID: %d  Nome do Estados: %s Nome do Fim: %s"%(i,self.estados[i].getNome(), self.fim[0]))
                return i

    def getFita(self):
        return self.fita

    def setInicio(self, inicio):
        self.inicio = inicio

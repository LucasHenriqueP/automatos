class SuperControle:
    def __init__(self, padraoEstados):
        self.padraoEstados = list()
        self.controles = list()

    def addControle(self, controle):
        self.controles.append(controle)

class Controle:
    def __init__(self, inicio, estados, fim):
        self.inicio = inicio
        self.estados = estados
        self.fim = fim

    def addEstado(self, estado):
        self.estados.append(estado)

    def addFim(self, fim):
        self.fim.append(fim)

    def getInicio(self):
        for i in range(len(self.estados)):
            if self.estados[i].getNome() == str(self.inicio):
               # print("ID: %d  Nome do Estados: %s Nome do Fim: %s"%(i,self.estados[i].getNome(), self.fim[0]))
                return i

    def setInicio(self, inicio):
        self.inicio = inicio

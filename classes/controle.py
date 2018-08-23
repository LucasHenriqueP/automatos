class Controle:
    def __init__(self, inicio):
        self.inicio = inicio
        self.estados = list()
        self.fim = list()

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

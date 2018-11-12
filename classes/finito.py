class Finito:
    def __init__(self, alfabeto, epson, final):
        self.alfabeto = alfabeto
        self.epson = epson
        self.final = final
        self.estados = []
        pass

    def addEstado(self, estado):
        self.estados.append(estado)

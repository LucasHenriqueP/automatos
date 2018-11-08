class Finito:
    def __init__(self, alfabeto, epson, inicial, final):
        self.alfabeto = alfabeto
        self.epson = epson
        self.inicial = inicial
        self.final = final
        self.estados = []
        pass

    def addEstado(self, estado):
        self.estados.append(estado)

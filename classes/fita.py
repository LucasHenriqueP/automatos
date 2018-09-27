class fita:
    def __init__(self, conteudo, alfabeto):
        conteudo = list(conteudo)
        self.conteudo = conteudo
        self.alfabeto = list(alfabeto)

    def getElemento(self):
        return self.conteudo[0]

    def removeElemento(self):
        self.conteudo.remove(0)   


f = fita("entrada", "ab")
print(f.conteudo)
print(f.alfabeto)  
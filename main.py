class Fita:
    def __init__(self, conteudo, pos, alfabeto):
        self.conteudo = list(conteudo)
        self.pos = pos
        self.alfabeto = alfabeto
    def __str__(self):
        return "Conteudo da Fita é %s\nE a cabeça de leitura está na posição %d" % (self.conteudo, self.pos)
    def getConteudo(self):
        return self.conteudo[self.pos]
    def setConteudo(self, novo):
        self.conteudo[self.pos] = novo
    def mover(self, novo, direcao):
        direcao.upper()
        if direcao == 'R':
            self.setConteudo(novo)
            self.pos += 1
        elif direcao == 'L':
            setConteudo(novo)
            self.pos -= 1


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

class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.trans = list()

    def addTransicao(self, trans):
        self.trans.append(trans)

class Controle:
    def __init__(self, inicio):
        self.inicio = inicio
        self.estados = list()

    def addEstado(self, estado):
        self.estados.append(estado)

# TESTANDO TUDO
fita = Fita('abbcc', 0, 'abcB#')
print(fita)
print(fita.getConteudo())
fita.mover('#', 'R')
print(fita.getConteudo())
print(fita)

trans = Transicao('a', '#', 'D', '2')
#print(trans)

q0 = Estado('0')
q0.addTransicao(trans)
for i in range(len(q0.trans)):
    print(q0.trans[i])

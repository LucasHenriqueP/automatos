import sys
import string


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
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.estados = list()
        self.fim = fim

    def addEstado(self, estado):
        self.estados.append(estado)

def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    #entrada = list(entrada)
    print(type(entrada))
    f = open(arq, 'r')
    line = f.readline()
    line = f.readline()
    alfabeto = line.replace(' ', '')
    #alfabeto = list(alfabeto)
    print(type(alfabeto))
    count = 0
    for i in range(len(entrada)):
        for j in range(len(alfabeto)):
            if entrada[i] == alfabeto[j]:
                count += 1
    if count != len(entrada):
        print("ENTRADA NAO VALIDA")
        sys.exit()
    fita = Fita(entrada, 0, alfabeto)
    line = f.readline()
    line = f.readline()
    estados = line.replace(" ", "")
    line = f.readline()
    inicio = int(line)
    line = f.readline()
    control = Controle(inicio, line)
    for i in range(len(estados)):
        est = Estado(str(i))
        control.addEstado(est)
    line = f.readline()
    for line in f:
        trans = line.replace("\n", '')
        trans = trans.replace(" ", "")
        pos = int(trans[0])
        next = int(trans[1])
        transicao = Transicao(trans[2], trans[3], trans[4], next)
        control.estados[pos].addTransicao(transicao)
  
    for i in range(len(control.estados)):
        for j in range(len(control.estados[i].trans)):
            print(control.estados[i].trans[j])


def main():
    setup()
    # my code here

if __name__ == "__main__":
    main()

# TESTANDO TUDO

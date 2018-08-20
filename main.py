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
    
    def getNome(self):
        return self.nome

    def addTransicao(self, trans):
        self.trans.append(trans)

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
        return self.inicio

    def setInicio(self, inicio):
        self.inicio = inicio

def run(control, fita):
    print(fita)
    parada = 1
    while(parada):
        controle = control.estados[control.getInicio()]
        for i in range(len(control.fim)):
            if control.getInicio() == control.fim[i]:
                parada = 0
        for i in range(len(controle.trans)):
            if fita.getConteudo() == controle.trans[i].getDado() :
                
                fita.mover(controle.trans[i].getEscrever(),controle.trans[i].getDirecao())
                control.setInicio(controle.trans[i].getNextState())
                parada = 0            
    print(fita) 


def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    #entrada = list(entrada)
    #print(type(entrada))
    f = open(arq, 'r')
    line = f.readline()
    line = f.readline()
    alfabeto = line.replace(' ', '')
    #alfabeto = list(alfabeto)
    #print(type(alfabeto))
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
    line = f.readline() # linha 4 conjunto de estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    #print(estados[2])
    line = f.readline() #linha 5
    inicio = int(line)
    line = f.readline() #linha 6 conjunto finais
    line = line.replace("\n", "")
    finais = line.split(" ")
    #print(finais)
    control = Controle(inicio)
    for i in range(len(finais)):
        control.addFim(finais[i])
    for i in range(len(estados)):
        est = Estado(str(i))
        control.addEstado(est)
    line = f.readline()
    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")

        pos = int(trans[0])

        next = int(trans[1])

        transicao = Transicao(trans[2], trans[3], trans[4], next)
        control.estados[pos].addTransicao(transicao)

    for i in range(len(control.estados)):
        for j in range(len(control.estados[i].trans)):
            print("Sou o estado %d" %(i),  control.estados[i].trans[j])

    run(control, fita)

def main():
    setup()

    # my code here

if __name__ == "__main__":
    main()

# TESTANDO TUDO

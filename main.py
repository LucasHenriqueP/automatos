import sys
import string
from copy import deepcopy
from classes.machine import *
from classes.estados import *

def setup():
#----------------- Começo do Scraping --------------
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")

    f = open(arq, 'r')
    line = f.readline() #Linha 1 - Alfabeto de Entrada Fita
    alfaFita = line
    line = f.readline() #Linha 2 - Alfabeto de Entrada Pilha
    alfaPilha = line

    line = f.readline() #Linha 3 - Simbolo que representa o Branco
    line = line.replace("\n", '')
    branco = line

    line = f.readline() #Linha 4 - Simbolo Inicial da Pilha
    simboloInicial = line

    line = f.readline() #Linha 5 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados

    line = f.readline() #Linha 6 - Estado Inicial
    inicio = line

    line = f.readline() #Linha 7 - Estado Fnal
    fim = line

    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))

    #line = f.readline() #Linha 8 - Transiçoes
    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")
        pos = trans[0]

        transicao = Transicao(trans[1], trans[2], trans[4], trans[3])
        est[estados.index(pos)].addTransicao(transicao)

    m = machine(entrada,0 ,"B" , alfaFita, simboloInicial, 0, branco, alfaPilha, est, fim, inicio)

#----------------- Fim do Scraping --------------

    print(m.getFita())
    print(m.getBrancoP())
    run(m)

def run(machine):
    
    while (machine.getPosFita() != 'B'):

        print(machine.getPosFita())
        machine.setProxFita()



def main():
    setup();

if __name__ == "__main__":
    main()

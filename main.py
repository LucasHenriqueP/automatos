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
    simboloInicial = line.replace("\n", '')

    line = f.readline() #Linha 5 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados

    line = f.readline() #Linha 6 - Estado Inicial
    inicio = line.replace("\n", "")

    line = f.readline() #Linha 7 - Estado Fnal
    fim = line.replace("\n", "")

    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))

    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")
        pos = trans[0]
        nextState = estados.index(trans[3]) #Trabalho com o Indice nao o Nome
        transicao = Transicao(trans[1], trans[2], trans[4], nextState)
        est[estados.index(pos)].addTransicao(transicao)

    inicio = estados.index(inicio)
    fim = estados.index(fim)
    m = machine(entrada,0 ,"B" , alfaFita, simboloInicial, 0, branco, alfaPilha, est, fim, inicio)

#----------------- Fim do Scraping --------------

    run(m)

def run2(machine):

    while (machine.getEstadoAtual().getNome() != machine.getFim().getNome() or (machine.getPosFita() != machine.getBrancoF())):
        print('Pilha %s '%machine.getPilha())
        print('Estado Atual: %s'%machine.getEstadoAtual().getNome())

        if((machine.getPosFita() != machine.getBrancoF()) or machine.getPilhaVazia() == -1):

            if (machine.verificarT(machine.getPosFita(),machine.getPosPilha()) != -1):
                print('.')
            else:
                print("NAO ACHOU TRANSIÇÃO")
                exit(1)

        #print('Pilha %s '%machine.getPilha())
        #print('Estado Atual: %s'%machine.getEstadoAtual().getNome())

        #if machine.getEstadoAtual().getNome() == machine.getFim().getNome() and machine.getPilhaVazia() == -1:
        #    print('ACHOU ESTADO FINAL [%s]'%machine.getEstadoAtual().getNome())
        #    exit(1)

        #if((machine.getPosFita() == machine.getBrancoF()) and machine.getPilhaVazia() == -1):
        #    print('CHEGOU AO FIM DA FITA')
        #    exit(1)

def run(machine):
    while ( (machine.getPosFita() != machine.getBrancoF()) and ((machine.getEstadoAtual().getNome() != machine.getFim().getNome()) or (machine.getPilhaVazia() == -1) ) ):
        print('Pilha %s '%machine.getPilha())
        print('Estado Atual: %s'%machine.getEstadoAtual().getNome())
        existeTrans = machine.verificarT(machine.getPosFita(),machine.getPosPilha())

    print('\nPilha %s '%machine.getPilha())
    print('Estado Atual: %s'%machine.getEstadoAtual().getNome())

    if machine.getEstadoAtual().getNome() == machine.getFim().getNome() and machine.getPilhaVazia() == -1:
        print('ACHOU ESTADO FINAL [%s]'%machine.getEstadoAtual().getNome())
        exit(1)
    if(((machine.getPosFita() == machine.getBrancoF()) and machine.getPilhaVazia() == -1)):
        print('CHEGOU AO FIM DA FITA')
        exit(1)



def main():
    setup();

if __name__ == "__main__":
    main()

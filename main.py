import sys
import string
from copy import deepcopy
from classes.machine import *
from classes.estados import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

        if((machine.getPosFita() != machine.getBrancoF()) or machine.isPilhaVazia() == -1):

            if (machine.verificarT(machine.getPosFita(),machine.getPosPilha()) != -1):
                print('.')
            else:
                print("NAO ACHOU TRANSIÇÃO")
                exit(1)

        #print('Pilha %s '%machine.getPilha())
        #print('Estado Atual: %s'%machine.getEstadoAtual().getNome())

        #if machine.getEstadoAtual().getNome() == machine.getFim().getNome() and machine.isPilhaVazia() == -1:
        #    print('ACHOU ESTADO FINAL [%s]'%machine.getEstadoAtual().getNome())
        #    exit(1)

        #if((machine.getPosFita() == machine.getBrancoF()) and machine.isPilhaVazia() == -1):
        #    print('CHEGOU AO FIM DA FITA')
        #    exit(1)

def run(machine):
    while ( (machine.getPosFita() != machine.getBrancoF()) and ((machine.getEstadoAtual().getNome() != machine.getFim().getNome()) or (machine.isPilhaVazia() == -1) ) ):
        print('-FITA [%s] '%machine.getPosFita())
        print('-Pilha %s '%machine.getPilha())
        print('-Estado Atual: %s'%machine.getEstadoAtual().getNome())
        print('\n')
        existeTrans = machine.verificarT(machine.getPosFita(),machine.getPosPilha())

    print('--FITA [%s] '%machine.getPosFita())
    print('--Pilha %s '%machine.getPilha())
    print('--Estado Atual: %s'%machine.getEstadoAtual().getNome())

    if machine.getEstadoAtual().getNome() == machine.getFim().getNome() and (machine.getPosFita() == machine.getBrancoF()):
        print(bcolors.OKGREEN+'\nACHOU ESTADO FINAL [%s]'%machine.getEstadoAtual().getNome()+bcolors.ENDC)
        exit(1)

    print('\n\n--aab : %d '%machine.isPilhaVazia())
    print('--TOPO PILHA : %s '%machine.getPosPilha())
    print('--PILHA INTEIRA: %s '%machine.getPilha())
    print('--PILHA TAM: %d '%machine.pos_pilha)

    if(((machine.getPosFita() == machine.getBrancoF()) and machine.isPilhaVazia() == -1)):
        print(bcolors.OKGREEN+'\nCHEGOU AO FIM DA FITA'+bcolors.ENDC)
        exit(1)

    elif machine.isPilhaVazia() == 1:
        print(bcolors.FAIL+'\nNÃO ACHOU TRANSAÇÃO'+bcolors.ENDC)
        exit(1)



def main():
    setup();

if __name__ == "__main__":
    main()

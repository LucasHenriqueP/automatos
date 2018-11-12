import sys
import string

from classes.estados import *
from classes.transicao import *
from classes.finito import *

def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    f = open(arq, 'r')

    alfabetoEntrada = f.readline() #Linha 1 - Alfabeto de Entrada


    epsilon = f.readline() #Linha 2 - Simbolo a ser considerado para representar epsilon ou lambda
    epsilon = epsilon.replace("\n",'')


    line = f.readline() #Linha 3 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados

    line = f.readline() #Linha 4 - Estado Inicial
    estadoInicio = line.replace("\n", "")

    line = f.readline() #Linha 5 - Conjunto de Estados de Aceitacao
    line = line.replace("\n", "")
    estadosAceitacao = line.split(" ")
    estadosAceitacao.sort() #Ordena os Estados

    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))

    for line in f:
        trans = line.replace("\n",'')
        trans = line.split(" ")
        pos = trans[0]

        a = trans[2].replace("\n",'')
        nextS = estados.index(a)

        transicao = Transicao(trans[0], trans[1], nextS)
        est[estados.index(pos)].addTransicao(transicao)

    automatoFinito = Finito(alfabetoEntrada, epsilon, estadoInicio, estadosAceitacao)
    automatoFinito.addEstado(est)
    for Estados in automatoFinito.estados[0]:
        print('\n')
        print(Estados.nome)
        for tr in Estados.transicao:
            print(tr)
    run(automatoFinito, entrada)


def run(finito, entrada):

    for estado in finito.estados[0]:
        if estado.nome == finito.inicial:
            estAtual = estado
            break

    print("Estado inicial: %s" %(estAtual.nome))
    entrada = list(entrada)
    print(entrada)

#While  #Ou estado de aceitacao ou não houver mais transicao e a fita e fita vazia


    for trans in estAtual.transicao:

        if(trans.isValida(entrada[0])) or (trans.isValida(finito.epson)):
            if(not(trans.isValida(finito.epson))):
                entrada.pop(0)

            for estad in finito.estados:
                for est in estad:
                    estAtual = estad[trans.getproximoEstado()]

    print("Entrada: %s" %(entrada))
    print("Estado Novo: %s" %(estAtual.nome))





def main():
    setup()

if __name__ == "__main__":
    main()

import sys
import string

from classes.estados import *
from classes.transicao import *
from classes.finito import *
from classes.contexto import *

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

    automatoFinito = Finito(alfabetoEntrada, epsilon, estadosAceitacao)
    automatoFinito.addEstado(est)
    for Estados in automatoFinito.estados[0]:
        print('\n')
        print(Estados.nome)
        for tr in Estados.transicao:
            print(tr)

    cont = Contexto(entrada,estados.index(estadoInicio))
    contextos = list()
    contextos.append(cont)

    run(automatoFinito, contextos)


def run(finito, contextos):

    while(len(contextos) > 0):

        i = contextos[0].estadoAtual
        estAtual = finito.estados[0]
        estAtual = estAtual[i]
        print("Estado inicial: %s" %(estAtual.nome))
        entrada = contextos[0].entrada
        print(entrada)

        noTransition = 1
        estadoFinal = 0

        while(1):

            if(len(entrada) == 0 and estadoFinal == 1):
                print("Fim da Fita e encontrou Estado final")
                exit(0)

            if(noTransition == 0):
                print("Sem transicao")
                contextos.pop(0)
                break

            noTransition = 0

            for trans in estAtual.transicao:
                if len( entrada ) != 0:
                    if(  trans.isValida(entrada[0])) or (trans.isValida(finito.epson) ):
                        noTransition = noTransition + 1





            for trans in estAtual.transicao:
                if len( entrada ) != 0:
                    if(  trans.isValida(entrada[0])) or (trans.isValida(finito.epson) ):
                        noTransition = noTransition + 1
                        if(not(trans.isValida(finito.epson))):
                            entrada.pop(0)

            for estad in finito.estados:
                for est in estad:
                    estAtual = estad[trans.getproximoEstado()]
                        cont = Contexto(entrada,estados.index(estadoInicio))
                        contextos.append(cont)

            for final in finito.final:
                print("Estado FINAL: %s ATUAL %s" %(final,estAtual.nome))
                if estAtual.nome == final:
                    print("Encontrou um Estado Final")
                    estadoFinal = 1

        print("Entrada: %s" %(entrada))
        print("Estado Atual: %s" %(estAtual.nome))
        print("Numero de Transições encontradas: %d" %(noTransition))


def main():
    setup()

if __name__ == "__main__":
    main()

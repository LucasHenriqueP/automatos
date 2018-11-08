import sys
import string
from classes.estados import *

def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    f = open(arq, 'r')
    
    alfabetoEntrada = f.readline() #Linha 1 - Alfabeto de Entrada
    
    epsilon = f.readline() #Linha 2 - Símbolo a ser considerado para representar epsilon ou lambda
    
    line = f.readline() #Linha 3 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados
    
    line = f.readline() #Linha 4 - Estado Inicial
    estadoInicio = line.replace("\n", "")
    
    line = f.readline() #Linha 5 - Conjunto de Estados de Aceitação
    line = line.replace("\n", "")
    estadosAceitacao = line.split(" ")
    estadosAceitacao.sort() #Ordena os Estados
    
    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))
        
     for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")
        pos = trans[0]
       # nextState = estados.index(trans[3]) #Trabalho com o Indice nao o Nome
        #transicao = Transicao(trans[1], trans[2], trans[4], nextState)
       # est[estados.index(pos)].addTransicao(transicao)

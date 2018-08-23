import sys
import string

from classes.fita import Fita
from classes.estado import *
from classes.controle import Controle



def run(control, fita):
    parada = 1
    #fita.mover('B', 'R')
    while(parada):
        controle = control.estados[control.getInicio()]
        for i in range(len(control.fim)):
            if control.estados[control.getInicio()].getNome() == str(control.fim[i]): #Se o Inicio esta em um dos Estados de Fim
                parada = 0
                print("ENCONTROU O ESTADO FINAL [%s]"%(control.fim[i]))
                exit(0)
        if parada != 0:
            print(fita)
            for i in range(len(controle.trans)):
                parada = 0; #Linha Caso o IF abaixo não encontre o dado no Estado Atual, ira Crashar/Sair
                if fita.getConteudo() == controle.trans[i].getDado() :
                    fita.mover(controle.trans[i].getEscrever(),controle.trans[i].getDirecao())
                    control.setInicio(controle.trans[i].getNextState())
                    print('Estado Atual [%d] -Antigo [%s] -  Foi Escrito [%s] - A Direção [%s]'%(control.getInicio(),controle.trans[i].getDado(), controle.trans[i].getEscrever(),controle.trans[i].getDirecao()))
                    parada = 1      #Se encontrar o dado na tabela de Transição ira continuar
                    break
    print(fita)

def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    f = open(arq, 'r')
    line = f.readline()
    line = f.readline()
    alfabeto = line.replace(' ', '')
    count = 0
    for i in range(len(entrada)):
        for j in range(len(alfabeto)):
            if entrada[i] == alfabeto[j]:
                count += 1
    if count != len(entrada):
        print("ENTRADA NAO VALIDA")
        sys.exit()

    line = f.readline() # Linha 3, caracter que representa o branco
    line = line.replace("\n", '')
    fita = Fita(entrada, 1, alfabeto, line)
    fita.conteudo.append(fita.getBranco()) #Adiciona um Branco no Final
    fita.conteudo.insert(0, fita.getBranco())

    line = f.readline() # linha 4 conjunto de estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados = list(map(int, estados))
    estados.sort()
    print(estados)
    line = f.readline() #linha 5
    inicio = int(line)
    line = f.readline() #linha 6 conjunto finais
    line = line.replace("\n", "")
    finais = line.split(" ")
    control = Controle(inicio)
    for i in range(len(finais)):
        control.addFim(finais[i])
    for i in range(len(estados)):
        est = Estado(str(estados[i]))
        control.addEstado(est)
    line = f.readline()
    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")

        pos = int(trans[0])
        next = int(trans[1])

        transicao = Transicao(trans[2], trans[3], trans[4], next)
        control.estados[pos].addTransicao(transicao)

#    for i in range(len(control.estados)):
#        for j in range(len(control.estados[i].trans)):
#            print("Sou o estado %d" %(i),  control.estados[i].trans[j])

    run(control, fita)

def main():
    setup()



if __name__ == "__main__":
    main()

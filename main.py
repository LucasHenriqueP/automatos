import sys
import string

from classes.fita import Fita
from classes.estado import *
from classes.controle import Controle

def run(control, fita):
    parada = 1
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
    line = f.readline() #Linha 1 - Alfabeto de Entrada
    line = f.readline() #Linha 2 - Alfabeto da Fita
    alfabeto = line.replace(' ', '')
    count = 0

    for i in range(len(entrada)):
        for j in range(len(alfabeto)):
            if entrada[i] == alfabeto[j]:
                count += 1

    if count != len(entrada):
        print("ENTRADA NAO VALIDA")
        sys.exit()

    line = f.readline() #Linha 3 - Simbolo que representa o Branco
    line = line.replace("\n", '')
    fita = Fita(entrada, 1, alfabeto, line)
    fita.conteudo.append(fita.getBranco()) #Adiciona um Branco no Final
    fita.conteudo.insert(0, fita.getBranco()) #Adiciona um Branco no Inicio

    line = f.readline() #Linha 4 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados = list(map(int, estados))
    estados.sort() #Ordena os Estados

    line = f.readline() #Linha 5 - Estado Inicial
    inicio = int(line)

    line = f.readline() #Linha 6 - Conjunto de Estados Finais
    line = line.replace("\n", "")
    finais = line.split(" ")

    est = list()
    for i in range(len(estados)):
        est.append(Estado(str(estados[i])))
        
    superEstados = SuperEstado(est, finais);

    control = Controle(inicio, superEstados.getEstados(), superEstados.getFinais())

    line = f.readline() #Linha 7 - Quantidade de Fitas

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

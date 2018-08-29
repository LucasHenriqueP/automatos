import sys
import string

from classes.fita import Fita
from classes.estado import *
from classes.controle import *
from copy import deepcopy

def run(control, SuperControle, SuperEstado):
    fita = control.getFita()
    print('Controler Atual [%d] -------- \n'%SuperControle.getAtual())
    while(1):

        #input('Pressione Qualquer Tecla para avançar!')
        tmp = 0
        possiveistransicoes = list()
        controle = control.estados[control.getInicio()]

        for i in range(len(control.fim)):
            if control.estados[control.getInicio()].getNome() == str(control.fim[i]): #Se o Inicio esta em um dos Estados de Fim
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ENCONTROU O ESTADO FINAL [%s]"%(control.fim[i]))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Controler [%d] encontrou fim!\n"%(SuperControle.getAtual()))
                return 0 #encontrou

        print(fita)

        for i in range(len(controle.trans)):

            if fita.getConteudo() == controle.trans[i].getDado() :
                tmp = tmp + 1
                possiveistransicoes.append(i)

        if tmp == 0 : #Se deu 0 não achou nenhuma transição naquele estado
            print("###################################Controler [%d] não encontrou fim/travou em um Estado!"%(SuperControle.getAtual()))
            print("###################################Estado [%s] Não encontrou nenhuma Transição!\n"%(controle.getNome()))
            return 1 #não existe transicoes disponiveis (Crashou)

        if tmp > 1 : #achou mais de uma transição
            for i in range(1,len(possiveistransicoes)): #adiciona no Vetor do SuperControle
                print('----------------------------------------------ADICIONOU FILHO')
                control2 = Controle(control.getInicio(), SuperEstado.getEstados(), SuperEstado.getFinais(),deepcopy(fita))
                control2.setInicio(controle.trans[possiveistransicoes[i]].getNextState())
                control2.fita.mover(controle.trans[possiveistransicoes[i]].getEscrever(),controle.trans[possiveistransicoes[1]].getDirecao())
                SuperControle.addControle(control2)

        fita.mover(controle.trans[possiveistransicoes[0]].getEscrever(),controle.trans[possiveistransicoes[0]].getDirecao()) #Continua fazendo a que estava fazendo
        control.setInicio(controle.trans[possiveistransicoes[0]].getNextState())
        print('Estado Atual [%d] -Antigo [%s] -  Foi Escrito [%s] - A Direção [%s]'%(control.getInicio(),controle.trans[possiveistransicoes[0]].getDado(), controle.trans[possiveistransicoes[0]].getEscrever(),controle.trans[possiveistransicoes[0]].getDirecao()))
        pass
    print(fita)

def run2(control, fita):
    parada = 1


    while(parada):
        controle = control.estados[control.getInicio()]
        for i in range(len(control.fim)):
            if control.estados[control.getInicio()].getNome() == str(control.fim[i]): #Se o Inicio esta em um dos Estados de Fim
                parada = 0
                print("ENCONTROU O ESTADO FINAL [%s]"%(control.fim[i]))
                #exit(0)
                return 0
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

#----------------- Começo do Scraping --------------
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

    control = Controle(inicio, superEstados.getEstados(), superEstados.getFinais(),fita)

    line = f.readline() #Linha 7 - Quantidade de Fitas

    for line in f:
        trans = line.replace("\n", '')
        trans = trans.split(" ")

        pos = int(trans[0])
        next = int(trans[1])

        transicao = Transicao(trans[2], trans[3], trans[4], next)
        control.estados[pos].addTransicao(transicao)

    superControle = SuperControle()
    superControle.addControle(control)

#----------------- Fim do Scraping --------------


#----------------- Começo do Run --------------
    while(run(superControle.getControle(), superControle, superEstados)):
        superControle.addAtual()
#----------------- Fim do Run -----------------


#----------------- Começo do Debug Visual --------------
    superControle.addAtual()
    superControle.atual = superControle.getAtual()-1

    for i in range(len(superControle.controles)):
        print('Controle[%d] - Conteudo = %s'%(i,superControle.controles[i].fita.conteudo));

#----------------- Fim do Debug Visual --------------


def main():
    setup()

if __name__ == "__main__":
    main()

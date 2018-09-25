class machine:
    def __init__(self,conteudo,pos_fita, branco_fita, alfabeto_fita, pilha, pos_pilha, branco_pilha, alfabeto_pilha, estados, fim, atual):

        #---- Começo Fita
        self.fita = list(conteudo)
        self.pos_fita = pos_fita
        self.branco_fita = branco_fita
        self.alfabeto_fita = list(alfabeto_fita)
        self.fita.append(self.branco_fita) #insere um Branco no Fim da Fita
        #----- Fim Fita

        #---- Comeco da Pilha
        self.pilha = pilha
        self.pos_pilha = pos_pilha
        self.branco_pilha = branco_pilha
        self.alfabeto_pilha = list(alfabeto_pilha)
        #--- Fim da Pilha

        #--- Começo Estados
        self.estados = estados #Objeto
        self.fim = fim #lista inteiros
        self.atual = atual #indice
        #--- Fim Estados

    def getFita(self): #Pega todo o Conteudo da Fita
        return self.fita

    def getPosFita(self): #Pega o Elemento que a Cabeça da Fita esta apontando
        return self.fita[self.pos_fita]

    def setProxFita(self): #Cabeça Avança
        self.pos_fita += 1

    def getPosPilha(self): #Pega o Elemento que esta no Topo da Pilha
        return self.pilha[self.pos_pilha]

    def getBrancoP(self): #Saber qual é o Branco no caso o 'Z'
        return self.branco_pilha

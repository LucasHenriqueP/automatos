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
        self.pilha = list(pilha)
        self.pos_pilha = pos_pilha
        self.branco_pilha = branco_pilha
        self.alfabeto_pilha = list(alfabeto_pilha)
        self.pilhavazia = pilha #Recebe de Inicio o Z
        #--- Fim da Pilha

        #--- Começo Estados
        self.estados = estados #Objeto
        self.fim = fim #lista inteiros
        self.atual = atual #indice
        #--- Fim Estados

    def getPilhaVazia(self):
        if self.pilhavazia == self.getPilha():
            return 1
        else:
            return -1

    def getFita(self): #Pega todo o Conteudo da Fita
        return self.fita

    def getPilha(self):
        return self.pilha

    def getPosFita(self): #Pega o Elemento que a Cabeça da Fita esta apontando
        return self.fita[self.pos_fita]

    def setProxFita(self): #Cabeça Avança
        if (self.pos_fita+1) != len(self.fita):
            self.pos_fita += 1

    def getPosPilha(self): #Pega o Elemento que esta no Topo da Pilha
        return self.pilha[self.pos_pilha]

    def getBrancoF(self): #Saber qual é o Branco no caso o 'B'
        return self.branco_fita

    def getBrancoP(self): #Saber qual é o Branco no caso o 'Z'
        return self.branco_pilha

    def getEstadoAtual(self):
        return self.estados[self.atual]

    def getFim(self):
        return self.estados[self.fim]

    def pop(self):
        self.pilha.pop()
        if self.pos_pilha-1 != -1:
            self.pos_pilha -= 1

    def push(self, valor):
        self.pilha.pop()
        for i in range(len(valor), 0, -1):
            self.pilha.append(valor[i-1])
            if self.pos_pilha+1 != len(valor):
                self.pos_pilha += 1

    def verificarT(self, c_fitaAtual, c_pilhaAtual):
        retorno = self.getEstadoAtual().isTransicao(c_fitaAtual,c_pilhaAtual)

        if retorno == -1: #Caso Nao achar nenhuma trasição naquele estado
            return -1

        if self.getEstadoAtual().trans[retorno].getTroca() == self.getBrancoP(): #acaso dor Episoln
            self.pop()
        else: #Caso nao for Episolon
            self.push(self.getEstadoAtual().trans[retorno].getTroca())

        self.atual = self.getEstadoAtual().trans[retorno].getNextState() # Mudo para o Proximo Estado

        self.setProxFita()

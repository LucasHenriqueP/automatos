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

    def isPilhaVazia(self):
        print('Dentro do isPilhaVazia: ')
        print('pilhavazia (%s != %s ) <-- getPosPilha '%(self.pilhavazia,self.getPosPilha()))
        if self.pilhavazia != self.getPosPilha():
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
        self.pos_pilha = len(self.pilha)-1

    def push(self, valor):
        if valor[len(valor)-1] != self.pilhavazia:
            self.pilha.pop()

        for i in range(len(valor), 0, -1):
            if valor[i-1] != self.pilhavazia:
                self.pilha.append(valor[i-1])
            if self.pos_pilha+1 != len(valor):
                self.pos_pilha += 1

    def verificarT(self, c_fitaAtual, c_pilhaAtual):
        retorno, flag = self.getEstadoAtual().isTransicao(c_fitaAtual,c_pilhaAtual, self.getBrancoP())

        if retorno == -1: #Caso Nao achar nenhuma trasição naquele estado
            return -1
        if flag == 0: # achou(E,E,E) só manda avançar a cabeça da FITA
            self.setProxFita()
            self.atual = self.getEstadoAtual().trans[retorno].getNextState() # Mudo para o Proximo Estado
            return 0

        if self.getEstadoAtual().trans[retorno].getTroca() == self.getBrancoP(): #acaso dor Episoln
            print('Estado Atual ANTES POP: %s'%self.getEstadoAtual().getNome())
            print('PILHA ANTES DO POP %s '%self.getPilha())
            self.pop()
            print('PILHA DEPOIS DO POP %s '%self.getPilha())
        else : #Caso nao for Episolon

            print('Estado Atual ANTES PUSH: %s'%self.getEstadoAtual().getNome())
            print('PILHA ANTES DO PUSH %s '%self.getPilha())
            self.push(self.getEstadoAtual().trans[retorno].getTroca())
            print('PILHA DEPOIS DO PUSH %s '%self.getPilha())
        self.atual = self.getEstadoAtual().trans[retorno].getNextState() # Mudo para o Proximo Estado

        self.setProxFita()

        return 1

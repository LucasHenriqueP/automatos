class machine:
    def __init__(self,conteudo,pos_fita, branco_fita, alfabeto_fita, pilha, pos_pilha, branco_pilha, alfabeto_pilha, estados, fim, atual):

        #---- Começo Fita
        self.fita = list(conteudo)
        self.pos_fita = pos_fita
        self.branco_fita = branco_fita
        self.alfabeto_fita = list(alfabeto_fita)
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

    def getFita(self):
        return self.fita

    def getBrancoP(self):
        return self.branco_pilha

    def searchNome(self, nome):
        lista_nomes.index('Gomes')
        print('aaaaa')
        print(self.nome.index(nome))

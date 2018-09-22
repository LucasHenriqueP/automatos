class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.trans = list()

    def getNome(self):
        return self.nome

    def addTransicao(self, trans):
        self.trans.append(trans)

class Transicao:
    def __init__(self, c_fita, c_pilha, troca, nextState):

        self.c_fita = c_fita
        self.c_pilha = c_pilha
        self.troca = troca
        self.nextState = nextState

    def __str__(self):
        return "Conteudo da Fita %s\nConteudo da Pilha %s\nValor a ser Trocado %s\nProximo Estado %s" % (self.c_fita, self.c_pilha, self.troca, self.nextState)

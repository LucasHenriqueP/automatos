class Fita:
    def __init__(self, conteudo, pos, alfabeto, branco):
        self.conteudo = list(conteudo)
        self.pos = pos
        self.alfabeto = alfabeto
        self.branco = branco
    def __str__(self):
        return "Conteudo da Fita é %s\nE a cabeça de leitura está na posição %d \n" % (self.conteudo, self.pos)
    def getBranco(self):
        return self.branco
    def getConteudo(self):
        return self.conteudo[self.pos]
    def setConteudo(self, novo):
        self.conteudo[self.pos] = novo
    def mover(self, novo, direcao):
        direcao.upper()
        if direcao == 'R':
            tmp = self.pos+ 1
            if(tmp > len(self.conteudo)-1 ): #Caso A Maquina Queira adicionar Algo na Frente do Conteudo
                self.setConteudo(novo)
                self.conteudo.append(self.getBranco())
            else:
                self.setConteudo(novo)
            self.pos += 1

        elif direcao == 'L':
            tmp = self.pos-1
            if(tmp < 0):
                self.conteudo.insert(0,novo)
            else:
                self.setConteudo(novo)
                self.pos -= 1

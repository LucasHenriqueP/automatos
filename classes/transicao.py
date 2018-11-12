class Transicao:
    def __init__(self, estadoAtual,simbolo, proximoEstado ):
        self.estadoAtual = estadoAtual
        self.simbolo = simbolo
        self.proximoEstado = proximoEstado
        pass

    def isValida(self, simb):
        if self.simbolo == simb:
            return True
        else:
            return False
            pass

    def getproximoEstado(self):
        return self.proximoEstado

    def __str__(self):
        return ("Do estado %s para o estado %s com o simbolo %s" %(self.estadoAtual, self.proximoEstado, self.simbolo))

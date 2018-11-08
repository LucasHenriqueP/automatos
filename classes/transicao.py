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

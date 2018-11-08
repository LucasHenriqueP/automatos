def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    f = open(arq, 'r')
    alfabetoEntrada = f.readline() #Linha 1 - Alfabeto de Entrada
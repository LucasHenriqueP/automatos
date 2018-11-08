def setup():
    arq = sys.argv[1]
    entrada = sys.argv[2]
    entrada = entrada.replace(" ", "")
    f = open(arq, 'r')
    alfabetoEntrada = f.readline() #Linha 1 - Alfabeto de Entrada
    
    epsilon = f.readline() #Linha 2 - Símbolo a ser considerado para representar epsilon ou lambda
    
    line = f.readline() #Linha 3 - Conjunto de Estados
    line = line.replace("\n", "")
    estados = line.split(" ")
    estados.sort() #Ordena os Estados
    
    line = f.readline() #Linha 4 - Estado Inicial
    estadoInicio = line.replace("\n", "")
    
    line = f.readline() #Linha 5 - Conjunto de Estados de Aceitação
    line = line.replace("\n", "")
    estadosAceitacao = line.split(" ")
    estadosAceitacaos.sort() #Ordena os Estados

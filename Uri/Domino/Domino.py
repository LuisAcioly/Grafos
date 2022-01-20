numArestas = 0

def setCor(peças):

    cor = {}
    for i in peças.keys():
        cor.update({i : 'B'})
    return cor

def BFS(peças, v):
    global numArestas

    cor[v] = 'C'

    for i in peças[v]:
        numArestas = numArestas + 1
    cor[v] = 'P'

    return 0

while True:
    try:
        numArestas = 0
        num = int(input())
        peças = {}
        for i in range(num):
            p1, p2 = input().split()

            booleano = p2 in peças
            
            if(booleano == False):
                peças.update({p2 : []})   
            if(p1 in peças):
                peças[p1].append(p2) 
            else:
                vetor = [p2]
                peças.update({p1 : vetor})
            
        cor = setCor(peças)

        for j in peças.keys():
            if(cor[j] == 'B'):
                BFS(peças, j)
        print("Numero arestas: " + str(numArestas))

    except EOFError:
        break
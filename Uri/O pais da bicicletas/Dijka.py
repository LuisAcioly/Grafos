INFINITO = 100000000

def solucao(pai, grafo, origem, destino):
    aux = destino
    max = -1
    if(origem == destino):
        print(0)
    else:
        while(aux != origem):
            next = pai[aux]
            if(grafo[aux][next] > max):
                max = grafo[aux][next]
            aux = pai[aux]
        print(max)
    return 0

def minimo(dist, cor, tam):
    min = INFINITO

    for i in range(tam):
        if(cor[i] == 'B' and dist[i] <= min):
            min = dist[i]
            index = i
    
    return index

def dijkstra(grafo, origem, destino, nVertices):

    pai = [-1 for i in range(nVertices)]
    cor = ['B' for i in range(nVertices)]
    dist = [INFINITO for i in range(nVertices)]
    
    dist[origem] = 0
    
    u = origem

    for j in range(nVertices-1):
        u = minimo(dist, cor, nVertices)
        cor[u] = 'P'
        for i in range(nVertices):
            if(grafo[u][i] != [] and dist[u] + grafo[u][i] < dist[i]):
                dist[i] = dist[u] + grafo[u][i]
                pai[i] = u

    solucao(pai, grafo, origem, destino)
    return 0

def inicio(n, m):
    listaAdj = [[[] for j in range(n)] for i in range(n)]

    for i in range(m):
        vOrigem, vDestino, peso = input().split()

        origem = int(vOrigem) - 1
        destino = int(vDestino) - 1
        peso = int(peso)

        listaAdj[origem][destino] = peso
        listaAdj[destino][origem] = peso

    num = int(input())
        
    for i in range(num):
        origem, destino = input().split()
        origem = int(origem) - 1
        destino = int(destino) - 1    
        dijkstra(listaAdj, origem,destino, n)
    
    return 0

n, m = input().split()

m = int(m)
n = int(n)
instancia = 1

while(n != 0 and m != 0):
    print("Instancia " + str(instancia))
    if(n != 0 and m != 0):
        inicio(n, m)
    n, m = input().split()

    m = int(m)
    n = int(n)
    instancia = instancia+1


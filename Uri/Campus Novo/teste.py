INFINITO = 1000000

#codigo de prim
passou = []

def IniciaPrim(grafo):# n do indice , passou = bool para ver se ja foi adicionado
    passou = [ False for i in range(nVertices)]
    
    soma = Prim(grafo,0,passou)
    for i in passou:
        if passou[i] == False:
            print("impossivel")
            break
        else:
            print(soma)
            break

def MinimoPrim(grafo,nVertices,origem,passou):
    minimo = INFINITO
    vertice = 0
    for i in range(nVertices):
        if grafo[origem][i] < minimo and passou[i] == False :
            minimo = grafo[origem][i]
            vertice = i
    return vertice

def Prim(grafo, origem,passou):
    
    passou[origem] = True

    soma = 0
    nmr_vertices = nVertices

    while(nmr_vertices !=0):
        u = MinimoPrim(grafo,nVertices,origem,passou)
        if passou[u] == False:
            passou[u] = True
            soma += grafo[origem][u]
        origem = u
        nmr_vertices = nmr_vertices - 1
    return soma
    

while True:
    try:
        matrizAdj = []

        nVertice, nAresta = input().split()
        
        nArestas = int(nAresta)
        nVertices = int(nVertice)

        grafo = [[INFINITO for i in range(nVertices)]  for j in range(nVertices)]

        for i in range(nArestas):
                linha = []
                origem, destino, peso = input().split()
                
                origem = int(origem)
                destino = int(destino)
                peso = int(peso)
                
                grafo[origem-1][destino-1] = peso
                grafo[destino-1][origem-1] = peso

        IniciaPrim(grafo)

    except EOFError:
        break



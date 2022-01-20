INFINITO = 1000000

lista = []
nArestas = []
nVertices = []

nTestes = 0

grafo = []

while True:
    try:

        nVertice, nAresta = input().split()
        
        nAresta = int(nAresta)
        nVertice = int(nVertice)
        nArestas.append(nAresta)
        nVertices.append(nVertice)
          
        nTestes = nTestes + 1

        for i in range(nAresta):
                linha = []
                origem, destino, peso = input().split()
                
                origem = int(origem)
                destino = int(destino)
                peso = int(peso)
                
                linha.append(origem)
                linha.append(destino)
                linha.append(peso)
                lista.append(linha)
    except EOFError:
        break

grafo = [[] for i in range(nTestes)]

for j in range(nTestes):  # matriz de adjacencia sendo criada para qualquer numero de testes
    grafo[j] = [INFINITO for i in range(nVertices[j])]
    for k in range(nVertices[j]):
            grafo[j][k] = [INFINITO for i in range(nVertices[j])]

inicio = 1
fim = nArestas[0]+1

for i in range(nTestes): 

    for j in range(inicio, fim):
        linha = lista[j]
        grafo[i][linha[0]-1][linha[1]-1] = linha[2]
        grafo[i][linha[1]-1][linha[0]-1] = linha[2]

    inicio = fim + 1
    if(i == nTestes-1):
         fim = fim + nArestas[i] + 1
    else:    
         fim = fim + nArestas[i+1] + 1

#codigo de prim
passou = []

def IniciaPrim(grafo,teste):# n do indice , passou = bool para ver se ja foi adicionado
    passou = [ False for i in range(nVertices[teste])]
    
    soma = Prim(grafo , teste ,0,passou)
    for i in passou:
        if passou[i] == False:
            print("impossivel")
            break
        else:
            print(soma)
            break
    
def MinimoPrim(grafo,teste,nVertices,origem,passou):
    minimo = INFINITO
    vertice = 0
    for i in range(nVertices):
        if grafo[teste][origem][i] < minimo and passou[i] == False :
            minimo = grafo[teste][origem][i]
            vertice = i
    return vertice

def Prim(grafo ,teste , origem,passou):
    
    passou[origem] = True

    soma = 0
    nmr_vertices = nVertices[teste]

    while(nmr_vertices !=0):
        u = MinimoPrim(grafo,teste ,nVertices[teste],origem,passou)
        if passou[u] == False:
            passou[u] = True
            soma += grafo[teste][origem][u]
        origem = u
        nmr_vertices = nmr_vertices - 1
    return soma

for j in range(nTestes):
    IniciaPrim(grafo,j)
    


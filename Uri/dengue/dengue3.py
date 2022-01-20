INF = 1000000000

def solve(grafo, tam):
    menor = INF
    caminho = []
    i = 0
    visitado = [0 for i in range(tam+1)]
    visitado[0] = 1

    caminho.append(0)

    while(0 in visitado):
        for i in caminho:
            for j in caminho:
                for k in range(tam+1):
                    if(menor >= grafo[i][k][1] + grafo[j][k][1] and visitado[k] == 0):
                        menor = grafo[i][k][1] + grafo[j][k][1]
                        id_menor = k
                        print(id_menor)
        
        print(menor)
        caminho.append(id_menor)
        visitado[id_menor] = 1

    print(caminho)

    return 0

def calcula_pesos(lista_de_arestas, lista_de_vertices):
    pesos = []

    for aresta in lista_de_arestas:
        A = lista_de_vertices[aresta[0]]
        B = lista_de_vertices[aresta[1]]

        Xa = A[0]
        Ya = A[1]
        Xb = B[0]
        Yb = B[1]

        peso = (((Xb - Xa)**2) + ((Yb - Ya)**2)) ** (1/2)

        peso = round(peso, 2)

        pesos.append(peso)  

    return pesos

def cria_grafo(teste, lista_de_arestas, pesos):
    grafo = {}
    for vertice in range(teste):
        grafo[vertice] = []
    for i in range(len(lista_de_arestas)):
        aresta = lista_de_arestas[i]
        
        valores = (aresta[1], pesos[i])
       
        grafo[aresta[0]].append(valores)
    
    return grafo

def leitura_vetores(lista_de_vertices, teste):

    for i in range(teste):
        X, Y = input().split()

        X = int(X)
        Y = int(Y)

        coordenada = (X, Y)

        lista_de_vertices.append(coordenada)

    return lista_de_vertices

def cria_arestas(teste):
    for i in range(teste):
        for j in range(teste):
            aresta = (i, j)
            if(j != i):
                lista_de_arestas.append(aresta)
    
    return lista_de_arestas

teste = int(input())

while(teste > 0 and teste <= 15):
    lista_de_vertices = []
    lista_de_arestas = []
    
    Xjoao, Yjoao = input().split()

    Xjoao = int(Xjoao)
    Yjoao = int(Yjoao)

    coordenadaCasa = (Xjoao, Yjoao)

    lista_de_vertices.append(coordenadaCasa)

    lista_de_vertices = leitura_vetores(lista_de_vertices, teste)

    lista_de_arestas = cria_arestas(teste+1)

    pesos = calcula_pesos(lista_de_arestas, lista_de_vertices)

    grafo = cria_grafo(teste+1, lista_de_arestas, pesos)

    solve(grafo, teste)

    teste = int(input())

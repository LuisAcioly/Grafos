def DFS_Start(labirinto, N, M):
    global maiorDistancia
    caminho = 1
    for i in range(N):
        for j in range(M):
            if(labirinto[i][j] == '.'):
                print("Caminho: " + str(caminho))
                caminho = caminho+1
                maiorDistancia = 0
                DFS(labirinto, i, j, 0, N, M)

    print(maiorDistancia)
    return 0

def DFS(labirinto, i, j, t_atual, N, M):
    global maiorDistancia    

    labirinto[i][j] = '#'

    if(t_atual > maiorDistancia):
        maiorDistancia = t_atual
        print("A maior distancia " + str(maiorDistancia))
        print("Coordenada [" + str(i) + "] [" + str(j) + "]")

    vizinhos = getVizinhos(labirinto, i, j, N, M)

    for k in vizinhos:
        i = k[0]
        j = k[1]
        if(labirinto[i][j] == '.'):
            t_atual = t_atual + 1
            DFS(labirinto, i, j, t_atual, N, M)
        
    return 0

def getVizinhos(labirinto, i, j, N, M):
    iDeCima = i-1
    iDeBaixo = i+1
    jDaEsq = j-1
    jDaDir = j+1

    vizinhos = []
    
    if(iDeCima >= 0):
        umVizinho = [iDeCima, j]
        vizinhos.append(umVizinho)
    if(iDeBaixo < N):
        umVizinho = [iDeBaixo, j]
        vizinhos.append(umVizinho)
    if(jDaEsq >= 0):
        umVizinho = [i, jDaEsq]
        vizinhos.append(umVizinho)
    if(jDaDir < M):
        umVizinho = [i, jDaDir]
        vizinhos.append(umVizinho)

    return vizinhos

N, M = input().split()

N = int(N)
M = int(M)

while(N > 0 and M > 0):
    if(5 <= N <= 500 and 5 <= M <= 500):
        labirinto = []
        for i in range(N):
            entrada =input()
            coluna = list(entrada)
            labirinto.append(coluna)
        DFS_Start(labirinto, N, M)

    N, M = input().split()

    N = int(N)
    M = int(M)
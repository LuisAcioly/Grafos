'''arquivo = open('entrada.txt','r')
lista = arquivo.readlines()

#Definindo o numero de testes
aux = lista[0]
linha = aux.split()

nTestes =int (linha[0])

#Definindo o numero de arestas e vertices
aux = lista[1]
linha = aux.split()

nArestas = int (linha[1])
nVertices = int(linha[0])

#Definindo tamanho da lista
tamLista = len(lista)

#Criando conjunto de grafos
grafo = [[] for i in range(nTestes)]

#Criando grafos
for j in range(nTestes):
    grafo[j] = [[] for i in range(nVertices)]

#Definindo o inicio e o fim de cada grafo
inicio = 2
fim = nArestas+2

#Montando cada grafo presente no arquivo
for i in range(nTestes):

    for j in range(inicio, fim):
        aux = lista[j]
        linha = aux.split()
        grafo[i][int (linha[0])].append(int (linha[1]))
    inicio = fim
    fim = fim + nArestas

INFINITO = 1000000000

t_atual = 0

espaço = ["  "]

nEspaço = 1

cor = [[] for i in range(nTestes)]
desc = [[] for i in range(nTestes)]
fecha = [[] for i in range(nTestes)]

for i in range(nTestes):
    cor[i] = ['B' for j in range(nVertices)]
    desc[i] = [INFINITO for j in range(nVertices)]
    fecha[i] = [INFINITO for j in range(nVertices)]

def DFS_Start():
    for i in range(nTestes):
        global t_atual
        t_atual = 0
        global nEspaço
        nEspaço = 1
        global espaço
        espaço = ["  "]
        print("Caso ", i+1,":")
        DFS(i)

def DFS(i):
    for j in range(nVertices):
        global nEspaço
        nEspaço = 1
        global espaço
        espaço = ["  "]
        if(cor[i][j] == 'B' and grafo[i][j] != []):   
            DFS_Detec(i, j)

def DFS_Detec(i, j):
    global t_atual
    global nEspaço
    #global espaço

    visitado = False

    cor[i][j] = 'C'
    desc[i][j] = t_atual

    t_atual = t_atual + 1
        
    vizinhos = grafo[i][j]

    for u in vizinhos:

        if(cor[i][u] == 'B'):
            visitado = False
            cor[i][u] = 'C'
            desc[i][u] = t_atual
            pathR(j, u, visitado)
            nEspaço = nEspaço+1
            DFS_Detec(i, u)
        else:
            visitado = True
            pathR(j, u, visitado)

    cor[i][j] = 'P'
    fecha[i][j] = t_atual
    t_atual = t_atual+1    
    nEspaço = nEspaço-1

def pathR(j, u, visitado):
    espaço = j, "-", u, "pathR(G,", u,')'
    global nEspaço

    for i in range(nEspaço):
        espaço.append("  ")
    
    espaço = ''.join(espaço)

    if(visitado):
        print(espaço, j, "-", u)
    else:
        print(espaço, j, "-", u, "pathR(G,", u,')')
    
    espaço = ["  "]


DFS_Start()
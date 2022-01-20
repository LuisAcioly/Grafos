#Questao URI mania do par
#O problema consiste em passar no menor numero de pedagios, porem sempre em numero par.
#Para a sua resolução foi utilizada uma BFS que calculava a distancia , se a tivesse passado por par pedagios
#imprime o valor da distancia , caso contrario imprime o valor de -1

#@author Walisson Mendes Ferreira
#@author Luis Wagner Acioly Bastos

#-UFLA Universidade Federal de Lavras-
#Algoritmos em Grafos
#Professor Mayron Moreira


INF = 100000000

#Após o calculo dos pais feito na BFS é somada os valores das arestas percorridas
def solução(grafo, destino, pai):
    soma = 0
    t_atual = destino

    #A função começa do destino e vai até a origem percorrendo os pais de cada vertice
    while(pai[t_atual] != -1):
        for i in grafo[t_atual]:
            if(i[0] == pai[t_atual]):
                soma = soma + i[1]
                t_atual = pai[t_atual]

    print(soma) 


#Função que realiza a Busca em largura padrao
def BFS(g, destino):
    tam = len(g)+1

    cor = ['B' for i in range(tam)]
    pai = [-1 for i in range(tam)]
    dist = [INF for i in range(tam)]

    cor[1] = 'C'
    dist[1] = 0

    Q = []
    Q.append(1)

    while(Q != []):
        u = Q.pop(0)

        for i in g[u]:
            if(cor[i[0]] == 'B'):
                cor[i[0]] = 'C'
                pai[i[0]] = u
                dist[i[0]] = dist[u] + 1
                Q.append(i[0])
        cor[u] = 'P'

    if(dist[destino]%2 == 0):
        solução(g, destino, pai)
    else:
        print(-1) 

#Função que recebida uma lista de arestas monta o grafo usando um dicionario
def cria_grafo(listaDeArestas):
    grafo = {}

    #For que percorre cada aresta na lista de arestas 
    for i in listaDeArestas:
        #Se a origem e o destino do vertice estiverem no grafo é criada a arestas
        if(i[0] in grafo and i[1] in grafo):
            dados = (i[1], i[2])
            grafo[i[0]].append(dados)
            dados2 = (i[0], i[2])
            grafo[i[1]].append(dados2)
        else:
            #Caso tenha o vertice origem mas não o destino, é criado o vertice destino e então é criada a aresta
            if(i[0] in grafo and (i[1] in grafo) == False):
                grafo[i[1]] = []
                dados = (i[1], i[2])
                grafo[i[0]].append(dados)
                dados2 = (i[0], i[2])
                grafo[i[1]].append(dados2)
            #Caso não tenha a origem e tenha o destino, é criado o vertice origem e então é criada a aresta
            elif((i[0] in grafo) == False and i[1] in grafo):            
                grafo[i[0]] = []
                dados = (i[1], i[2])
                grafo[i[0]].append(dados)
                dados2 = (i[0], i[2])
                grafo[i[1]].append(dados2)
            #Caso nenhum vertice exista é criado os dois e então é criada a aresta
            else:
                grafo[i[0]] = []
                grafo[i[1]] = []
                dados = (i[1], i[2])
                grafo[i[0]].append(dados)
                dados2 = (i[0], i[2])
                grafo[i[1]].append(dados2)

    return grafo

#Entrada do numero de vertices, arestas e o vertice destino
destino,nArestas = input().split()

#Conversão para inteiro
destino = int(destino)
nArestas = int(nArestas)

listaDeArestas = []

#Leitura das arestas
for i in range(nArestas):
    vOrigem,vDestino,peso = input().split()

    vOrigem = int(vOrigem)
    vDestino = int(vDestino)
    peso = int(peso)

    dados = [vOrigem, vDestino, peso]

    listaDeArestas.append(dados)

grafo = cria_grafo(listaDeArestas)

BFS(grafo, destino)
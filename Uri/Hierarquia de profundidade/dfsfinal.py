#Definindo o numero de testes
nTestes = int(input())

#Criando lista com numero de teste 
grafo = [[] for i in range(nTestes)]

#Numero de vertice e arestas 
nArestas = [[] for i in range(nTestes)]
nVertices = [[] for i in range(nTestes)]

#Montando cada grafo presente no arquivo e adicionando a uma lista de adjacencia
for i in range(nTestes):
    nVertice, nAresta = input().split()   
    #Lista que armazena a quantidade de arestas de cada teste
    nArestas[i] = int(nAresta)
    #Lista que armazena a quantidade de vertice de cada teste
    nVertices[i] = int(nVertice)

    grafo[i] = [[] for i in range(nVertices[i])]

    for j in range(nArestas[i]):
        vOrigem, vDestino = input().split()
        #Vertice de origem da aresta
        vOrigem = int(vOrigem)
        #Vertice de destino da aresta
        vDestino = int(vDestino)
        #Inserindo a aresta na lista de adjacencia do respectivo grafo
        grafo[i][vOrigem].append(vDestino)

#variavel para inicializar tempo de descoberta e tempo de fechamento
INFINITO = 1000000000

#tempo global
t_atual = 0

#numero de espacos da hierarquia inicial
nEspaço = 2

#criando listas para cada teste
cor = [[] for i in range(nTestes)]
desc = [[] for i in range(nTestes)]
fecha = [[] for i in range(nTestes)]

#inicializando listas com valores iniciais
for i in range(nTestes):
    cor[i] = ['B' for j in range(nVertices[i])]
    desc[i] = [INFINITO for j in range(nVertices[i])]
    fecha[i] = [INFINITO for j in range(nVertices[i])]

#funcao que inicia a busca em grafos e tambem as impressoes da hierarquia
def DFS_Start():
    for i in range(nTestes):
        #Toda vez que é trocado o teste a hierarquia e o tempo atual  são resetados
        global t_atual
        t_atual = 0
        global nEspaço
        nEspaço = 2

        print("Caso ", i+1,":")
        #Chamada da DFS
        DFS(i)

#funcao que percorre todo o grafo enquanto houver vertice branco
def DFS(i):
    for j in range(nVertices[i]):
        #Quando um vertice é chamado aqui significa que um vertice foi fechado 
        # anteriormente(ou significa que a arvore em questão foi finalizada e outra foi encontrada) na DFS, portando a hierarquia é resetada
        global nEspaço
        nEspaço = 2

        if(cor[i][j] == 'B' and grafo[i][j] != []):   
            DFS_Detec(i, j)
            print("\n")

#funcao da busca em profundidade 
def DFS_Detec(i, j):
    global t_atual
    global nEspaço
#visitado informa se o vertice é branco , para a impressão da hierarquia
    visitado = False

    cor[i][j] = 'C'
    desc[i][j] = t_atual

    t_atual = t_atual + 1
        
    vizinhos = grafo[i][j]

    for u in vizinhos:

        if(cor[i][u] == 'B'):
            #Se um vertice vizinho é descoberto como branco, sua aresta é de arvore,
            #portanto a proxima aresta esta em outro nivel de hierarquia
            visitado = False
            cor[i][u] = 'C'
            desc[i][u] = t_atual
            #Chamada da função que irá escrever na tela a hierarquia
            pathR(j, u, visitado)
            #Acrescentando espaços na hierarquia
            nEspaço = nEspaço+2
            DFS_Detec(i, u)
        else:
            #Caso o vertice descoberto não seja branco, as unicas opções de hierarquia são:
            # A hierarquia continuar no mesmo nivel ou retornar para anterior
            visitado = True
            pathR(j, u, visitado)

    cor[i][j] = 'P'
    fecha[i][j] = t_atual
    t_atual = t_atual+1
    #Quando um vertice é fechado e se torna preto significa que ele não possui mais descendentes,
    # portanto devemos retornar na hierarquia    
    nEspaço = nEspaço-2


#funcao definida para adicionar os espacos respectivos  a cada  hieraquia
def pathR(j, u, visitado):
    global nEspaço
    
    #Frase que irá ser impressa
    if(visitado):
        frase = str(j) + " - " + str(u)
    else:
        frase = str(j) + " - " + str(u) + " pathR(G,"+ str(u) +")"

    #Com base no valor nEspaço calculado durante a DFS, podemos ajustar a hierarquia
    tamFrase=len(frase)+nEspaço  
    #A frase é reajustada com o novo tamanho
    frase=frase.rjust(tamFrase)
    print(frase)

#funcao que inicia a busca
DFS_Start()
qtd_testes = int(input())

lista_arquivo = []

lista_arquivo = input().split(" ")
nmr_vertices = int(lista_arquivo[0])
nmr_Arestas = int(lista_arquivo[1])

conjunto_lista = [[] for i in range(qtd_testes)]

for e in range(qtd_testes):
    conjunto_lista[e] = [[] for i in range(nmr_vertices)]




for w in range(0,qtd_testes):
    for i in range(0,nmr_Arestas):
        A,B = input().split()
        conjunto_lista[w][int(A)].append(int(B))
        
        
        

#origem onde comeca a busca em largura ,onde o valor vertice que ele comecara a busca
s = 0

#Defino infinito para tempo de descoberta e para tempo de fechamento
INFINITO = 100000

#tempo global
tempo = 0      
    

cor = ['B' for i in range(nmr_vertices)]
tempo_Descoberta = [INFINITO for i in range(nmr_vertices)]
tempo_Fechamento = [INFINITO for i in range(nmr_vertices)]
pai = [-1 for i in range(nmr_vertices)] 




#Funcao para encontrar vizinhos
#grafo e a lista de adjacencia , v e o vertice no qual estou e I e o indice da lista usada
def getVizinhos(v):
    return grafo[v]


#funcao da busca em profundidade (recursiva)
def DFS(grafo,v):
    # parte da Hierarquia
    global space
    global cont_space
    pathRCompleto = False

    global tempo
    tempo_Descoberta[v]=tempo
    tempo = tempo + 1

    #pego vizinhos 
    vizinhos = getVizinhos(v)
    for e in vizinhos:
        if cor[e] == 'B':
            cor[e]= 'C'
            pai[e]= v
            pathRCompleto = True
            pathR(v,e,pathRCompleto)
            cont_space = cont_space + 1
            DFS(grafo,e)
        elif cor[e] == 'P': 
            pathR(v,e,pathRCompleto)
    cont_space -= 1
    cor[v] = 'P'
    tempo_Fechamento[v]=tempo
    tempo = tempo +1
    return pai



#funcao para a impressao da hierarquia
def pathR(j, u,pathRCompleto):
    global space
    global cont_space

    for i in range(cont_space):
        space.append("  ")

    space = ''.join(space)

    if pathRCompleto == False:
        print(space,j,"-",u)
    else:
        print(space, j, "-", u, "pathR(G,", u,")")
    space = ["  "]
    
    


#funcao que testa os grafos com base no valor de testes passado no arquivo
for d in range(qtd_testes):
    print('Caso ',d+1,':')
    grafo = conjunto_lista[d] 
    tempo = 0
    cor = ['B' for i in range(nmr_vertices)]
    tempo_Descoberta = [INFINITO for i in range(nmr_vertices)]
    tempo_Fechamento = [INFINITO for i in range(nmr_vertices)]
    pai = [-1 for i in range(nmr_vertices)] 
    for e in range(nmr_vertices):
        if cor[e] == 'B':
            global cont_space
            global space
            cont_space=0
            space = ["  "]
            DFS(grafo,e)
            
    

#parte da impressao do resultado(python 3 so funcionou quando declarei eles abaixo da onde usei,nao entendi o porque)
#contador para averiguar o numero de espacos para cada hierarquia
cont_space = 0

#marcador de espacos brancos para a impressao
space = ["  "]

    












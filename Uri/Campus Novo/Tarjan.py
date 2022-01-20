def calculaAresta(lista, nTestes):
    nArestas = [[] for i in range(nTestes)]

    j = 0

    for i in range(nTestes):
        aux = lista[j]
        linha = aux.split()
        nArestas[i] = int(linha[1])
        j = j + int(linha[1]) + 1
    
    return nArestas

def calculaVertice(lista, nTestes):
    nVertices = [[] for i in range(nTestes)]

    j = 0

    for i in range(nTestes):
        aux = lista[j]
        linha = aux.split()
        nVertices[i] = int(linha[0])
        j = j + int(linha[1]) + 1
    
    return nVertices

def calculaTestes(lista, tamLista):
    i = 0
    nTestes = 0

    while(i < tamLista):
        aux = lista[i]
        linha = aux.split()
        i = i+int(linha[1])+1
        nTestes = nTestes + 1
        
    return nTestes

    
arquivo = open('entrada.txt','r')
lista = arquivo.readlines()

tamLista = len(lista)

nTestes = calculaTestes(lista, tamLista)

grafo = [[] for i in range(nTestes)]
peso =  [[] for i in range(nTestes)]

aux = lista[0]
linha = aux.split()

nArestas = calculaAresta(lista, nTestes)
nVertices = calculaVertice(lista, nTestes)

for j in range(nTestes):
    grafo[j] = [[] for i in range(nVertices[j])] 
    peso[j] = [[] for i in range(nVertices[j])]
    for k in range(nVertices[j]):
            peso[j][k] = [[] for i in range(nVertices[j])]

inicio = 1
fim = nArestas[0]+1

for i in range(nTestes):
    
    for j in range(inicio, fim):
        aux = lista[j]
        linha = aux.split()
        grafo[i][int (linha[0])-1].append(int (linha[1])-1)
        grafo[i][int (linha[1])-1].append(int (linha[0])-1)
        peso[i][int (linha[0])-1][int (linha[1])-1] = int(linha[2])
        peso[i][int (linha[1])-1][int (linha[0])-1] = int(linha[2])

    inicio = fim + 1
    if(i == nTestes-1):
         fim = fim + nArestas[i] + 1
    else:    
         fim = fim + nArestas[i+1] + 1


for j in range(nTestes):
    print("grafo " + str(j+1))
    for k in range(nVertices[j]):
        print(grafo[j][k])

for j in range(nTestes):
    print("matriz " + str(j+1))
    for k in range(nVertices[j]):
        print(peso[j][k])
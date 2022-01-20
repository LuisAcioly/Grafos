def imprimi(convidados):
    aux = 0

    sortedConvidados = sorted(convidados.keys())

    for i in sortedConvidados:
        if(convidados[i] == True):
            print(i, end=" ")
            aux = aux+1
    if(aux == 0):
        print(0)

    return 0

def BFS(grafo, convidados, cor, pai, numPessoas, minAmigos):

    Q = []
    Q.append(1)

    while(Q != []):
        u = Q.pop(0)

        if(len(grafo[u]) >= minAmigos):
            convidados[u] = True

        for i in grafo[u]:
            
            if(convidados[u] == True and len(grafo[i]) < minAmigos):
                convidados[u] = False
    
            if(cor[i] == 'B'):
                cor[i] = 'C'
                pai[i] = u
                Q.append(i)
        cor[u] = 'P'

    imprimi(convidados)

    return 0

def cria_grafo(lista_de_arestas, numPessoas, minAmigos):
    grafo = {}
    cor = {}
    pai = {}
    convidados = {}

    for aresta in lista_de_arestas:
        if(aresta[0] in grafo):
            grafo[aresta[0]].append(aresta[1])
        else:
            grafo[aresta[0]] = []
            grafo[aresta[0]].append(aresta[1])
            cor[aresta[0]] = 'B'
            convidados[aresta[0]] = False
            pai[aresta[0]] = -1

    BFS(grafo, convidados, cor, pai, numPessoas, minAmigos)

    return grafo

while True:
  try:
    numPessoas, numAmigos, minAmigos = input().split()

    numPessoas = int(numPessoas)
    numAmigos = int(numAmigos)
    minAmigos = int(minAmigos)

    lista_de_arestas = []

    for i in range(numAmigos):

        pessoa1, pessoa2 = input().split()

        pessoa1 = int(pessoa1)
        pessoa2 = int(pessoa2)

        aresta = (pessoa1, pessoa2)

        lista_de_arestas.append(aresta)

        aresta = aresta[::-1]

        lista_de_arestas.append(aresta)

    grafo = cria_grafo(lista_de_arestas, numPessoas, minAmigos)

  except EOFError:
    break
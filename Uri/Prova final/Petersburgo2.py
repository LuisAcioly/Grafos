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

while True:
  try:
    grafo = {}
    pai = {}
    cor = {}
    convidados = {}
    
    numPessoas, numAmigos, minAmigos = input().split()

    numPessoas = int(numPessoas)
    numAmigos = int(numAmigos)
    minAmigos = int(minAmigos)

    for i in range(numAmigos):

        pessoa1, pessoa2 = input().split()

        pessoa1 = int(pessoa1)
        pessoa2 = int(pessoa2)

        if(pessoa1 in grafo and pessoa2 in grafo):
            grafo[pessoa1].append(pessoa2)
            grafo[pessoa2].append(pessoa1)
        elif(pessoa1 in grafo and (pessoa2 in grafo) == False):
            grafo[pessoa2] = []
            pai[pessoa2] = -1
            cor[pessoa2] = 'B'
            convidados[pessoa2] = False
            grafo[pessoa1].append(pessoa2)
            grafo[pessoa2].append(pessoa1)
        elif((pessoa1 in grafo) == False and pessoa2 in grafo):
            grafo[pessoa1] = []
            pai[pessoa1] = -1
            cor[pessoa1] = 'B'
            convidados[pessoa1] = False
            grafo[pessoa1].append(pessoa2)
            grafo[pessoa2].append(pessoa1)
        else:
            grafo[pessoa2] = []
            pai[pessoa2] = -1
            cor[pessoa2] = 'B'
            convidados[pessoa2] = False
            grafo[pessoa1] = []
            pai[pessoa1] = -1
            cor[pessoa1] = 'B'
            convidados[pessoa1] = False
            grafo[pessoa1].append(pessoa2)
            grafo[pessoa2].append(pessoa1)
        
    BFS(grafo, convidados, cor, pai, numPessoas, minAmigos)

  except EOFError:
    break
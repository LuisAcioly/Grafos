def verificaAmigos(amigo, grafo, minAmigos):
    convidada = True
    
    for pessoa in amigo:
        
        qtdAmigos = len(grafo[pessoa])
        
        if(qtdAmigos < minAmigos):
            convidada = False

    return convidada

def solução(grafo, minAmigos):
    numConvidadas = 0
    for pessoa in grafo:
        qtdAmigos = len(grafo[pessoa])

        if(qtdAmigos >= minAmigos):
            convidado = verificaAmigos(grafo[pessoa], grafo, minAmigos)
            if(convidado):
                print(pessoa, end=(" "))
                numConvidadas = numConvidadas+1

    if(numConvidadas == 0):
        print(0)
    
    return 0

def cria_grafo(lista_de_arestas, numPessoas):
    grafo = {}

    for i in range(numPessoas+1):
        if(i != 0):
            grafo[i] = []

    for aresta in lista_de_arestas:
        
        grafo[aresta[0]].append(aresta[1])

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

    grafo = cria_grafo(lista_de_arestas, numPessoas)
    print(grafo)

    solução(grafo, minAmigos)

  except EOFError:
    break
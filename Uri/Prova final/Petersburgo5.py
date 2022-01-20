def solução(grafo, minAmigos):
    chaves = list(grafo.keys())
    print(chaves)
    print(len(grafo[5]))
    tam = len(chaves)
    for i in range(tam):
        if(i < len(chaves)):
            if not(len(grafo[chaves[i]]) >= minAmigos):
                chaves.remove(chaves[i])
    print(chaves)

    

while True:
  try:
    grafo = {}
    
    numPessoas, numAmigos, minAmigos = input().split()

    numPessoas = int(numPessoas)
    numAmigos = int(numAmigos)
    minAmigos = int(minAmigos)

    if(numPessoas >= 1 and numPessoas <= 1000):
        for i in range(numAmigos):

            pessoa1, pessoa2 = input().split()

            pessoa1 = int(pessoa1)
            pessoa2 = int(pessoa2)

            if(pessoa1 in grafo and pessoa2 in grafo):
                grafo[pessoa1].append(pessoa2)
                grafo[pessoa2].append(pessoa1)
            elif(pessoa1 in grafo and (pessoa2 in grafo) == False):
                grafo[pessoa2] = []
                grafo[pessoa1].append(pessoa2)
                grafo[pessoa2].append(pessoa1)
            elif((pessoa1 in grafo) == False and pessoa2 in grafo):
                grafo[pessoa1] = []
                grafo[pessoa1].append(pessoa2)
                grafo[pessoa2].append(pessoa1)
            else:
                grafo[pessoa2] = []
                grafo[pessoa1] = []
                grafo[pessoa1].append(pessoa2)
                grafo[pessoa2].append(pessoa1)
        solução(grafo, minAmigos)
 
  except EOFError:
    break
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
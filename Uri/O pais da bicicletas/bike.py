INFINITO = 10000000000

def Dijkstra(origem, listaAdj):
    pai = {}
    cor = {}
    valor = {}

    for i in listaAdj:
        pai.update({i : -1})
        cor.update({i : 'B'})
        valor.update({i : INFINITO})
    
    cor[origem] = 'P'
    valor[origem] = 0

    Q = []
    Q.append(origem)

    '''while(Q != []):
        u = Q.pop(0)
        for i in listaAdj[u]:'''
            

    
    return 0


listaAdj = {}

n, m = input().split()

m = int(m)

for i in range(m):
    vOrigem, vDestino, peso = input().split()

    if(i == 0):
        origem = vOrigem
    if(i == m-1):
        destino = vOrigem

    arestaIda = {"vDestino" : vDestino,
              "peso" : peso}
    arestaVolta = {"vDestino" : vOrigem,
              "peso" : peso}

    if(vOrigem in listaAdj):
        listaAdj[vOrigem].append(arestaIda)
    else:
        vetor = [arestaIda]
        listaAdj.update({vOrigem : vetor})
    if(vDestino in listaAdj):
        listaAdj[vDestino].append(arestaVolta)
    else:
        vetor = [arestaVolta]
        listaAdj.update({vDestino : vetor})

print(listaAdj['2'])
#Dijkstra(origem, listaAdj)



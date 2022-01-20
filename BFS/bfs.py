INFINITO = 1000000000

def criaGrafo():
    g = {   0 : [1, 3],
            1 : [0, 2, 4],
            2 : [1, 5],
            3 : [0, 4],
            4 : [1, 3, 5],
            5 : [2, 4],
    }
    return g

def imprimi(g):
    for v in g:
        print("O vertice", v ,"tem os vizinhos:")
        for u in g[v]:
            print(u, end=" ")
        print()

def BTS(grafo, o):

    cor = ['B' for i in range(6)]
    pai = [-1 for i in range(6)]
    dist = [INFINITO for i in range(6)]

    cor[o] = 'C'
    dist[o] = 0

    Q = []
    Q.append(o)

    while(Q != []):
        u = Q.pop(0)
        cor[u] = 'P'
        
        for v in grafo[u]:
            if(cor[v] == 'B'):
                cor[v] = 'C'
                pai[v] = u
                dist[v] = dist[u] + 1
                Q.append(v)

    for i in cor:
        print(i, end=" ")
    print()
    
    for i in pai:
        print(i, end=" ")
    print()

    for i in dist:
        print(i, end=" ")
    print()


g = criaGrafo()

print(g)



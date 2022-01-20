INFINITO = 1000000000

def criaGrafo():    
    g = {   0 : [1, 2, 3],
            1 : [0, 2],
            2 : [0, 1, 3, 5],
            3 : [0, 2, 4],
            4 : [3],
            5 : [2],   
        }
    return g
def BFS(g, v):
    cor = ['B' for i in range(6)]
    pai = [-1 for i in range(6)]
    dist = [INFINITO for i in range(6)]

    cor[v] = 'C'
    dist[v] = 0

    Q = []
    Q.append(v)

    while(Q != []):
        u = Q.pop(0)

        for i in g[u]:
            if(cor[i] == 'B'):
                cor[i] = 'C'
                pai[i] = u
                dist[i] = dist[u] + 1
                Q.append(i)
        cor[u] = 'P'

    print(cor)
    print(pai)
    print(dist)

    
g = criaGrafo()
BFS(g, 2)

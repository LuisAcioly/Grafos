def setPai(peças):

    pai = {}
    for i in peças.keys():
        pai.update({i : -1})
    return pai

def setCor(peças):

    cor = {}
    for i in peças.keys():
        cor.update({i : 'B'})
    return cor

def setDist(peças):

    dist = {}
    for i in peças.keys():
        dist.update({i : -1})
    return dist

def resposta(dist):

    print(max(dist.values(), key=int))

    return 0


def BFS(peças, v):
    pai = setPai(peças)
    cor = setCor(peças)
    dist = setDist(peças)

    cor[v] = 'C'
    dist[v] = 0

    Q = []
    Q.append(v)

    while(Q != []):
        u = Q.pop(0)

        for i in peças[u]:
            if(i != ' ' and cor[i] == 'B'):
                cor[i] = 'C'
                pai[i] = u
                dist[i] = dist[u] + 1
                Q.append(i)
        cor[u] = 'P'
    
    resposta(dist)

    return 0

while True:
    try:
        num = int(input())
        peças = {}
        for i in range(num):
            p1, p2 = input().split()
            
            if(i == 0):
                v = p1

            peças.update({p1 : p2})
            peças.update({p2 : ' '})
        BFS(peças, v)
    except EOFError:
        break
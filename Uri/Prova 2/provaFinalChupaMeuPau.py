def dijkstra(ori, dest, g):
	
    Q = []
    dist = [[INF, INF] for i in range(dest+1)]
	
    dist[1] = [0, INF]
	
    Q.append([0,1])
	
    while(Q != []):
        par = Q.pop(0)
        v = par[1]
		
        for i in range(len(g[v])):
			
            u = g[v][i]
			
            if(dist[v][0]+u[1]<dist[u[0]][1]):
                dist[u[0]][1]=dist[v][0]+u[1]
				
                Q.append([dist[u[0]][1], u[0]])
			
            if(dist[v][1]+u[1]<dist[u[0]][0]):
				
                dist[u[0]][0]=dist[v][1]+u[1]
                Q.append([dist[u[0]][0], u[0]])
	
    if(dist[dest][0]==INF): 
        return -1
	
    return dist[dest][0]

INF = 100000000

destino,nArestas = input().split()

destino = int(destino)
nArestas = int(nArestas)

grafo = {}

for i in range(nArestas):
    vOrigem,vDestino,peso = input().split()

    vOrigem = int(vOrigem)
    vDestino = int(vDestino)
    peso = int(peso)

    i = [vOrigem, vDestino, peso]

    if(i[0] in grafo and i[1] in grafo):
            dados = (i[1], i[2])
            grafo[i[0]].append(dados)
            dados2 = (i[0], i[2])
            grafo[i[1]].append(dados2)
    else:
        if(i[0] in grafo and (i[1] in grafo) == False):
            grafo[i[1]] = []
            dados = (i[1], i[2])
            grafo[i[0]].append(dados)
            dados2 = (i[0], i[2])
            grafo[i[1]].append(dados2)
        elif((i[0] in grafo) == False and i[1] in grafo):            
            grafo[i[0]] = []
            dados = (i[1], i[2])
            grafo[i[0]].append(dados)
            dados2 = (i[0], i[2])
            grafo[i[1]].append(dados2)
        else:
            grafo[i[0]] = []
            grafo[i[1]] = []
            dados = (i[1], i[2])
            grafo[i[0]].append(dados)
            dados2 = (i[0], i[2])
            grafo[i[1]].append(dados2)

print(dijkstra(1,destino, grafo))


INFINITO = 10000000

cor = ['B' for i in range(7)]
pai = [-1 for i in range(7)]
desc = [INFINITO for i in range(7)]
fecha = [INFINITO for i in range(7)]


t_atual = 0
continua = True

def criaGrafo():    
    g = {   0 : [1, 2],
            1 : [3],
            2 : [1],
            3 : [2],
            4 : [3 ,5],
            5 : [5],    
        }
    return g

def DFS_VISIT(grafo, s):
    global t_atual
    global continua

    desc[s] = t_atual
    print("Tempo de descobrimento do vertice ", s, " é ", t_atual)
    cor[s] = 'C'

    t_atual = t_atual+1

    for u in grafo[s]:
        if(cor[u] == 'B'):
            print("(", s, ",", u,") é uma arco de arvore")
            cor[u] = 'C'
            pai[u] = s
            DFS_VISIT(grafo, u)
        elif(cor[u] == 'C'):
             print("(", s, ",", u,") é uma arco de retorno")
             print("o grafo tem um ciclo")
        elif(cor[u] == 'P' and fecha[u] > desc[s]):
            print("(", s, ",", u,") é uma arco direto")
        else:
            print("(", s, ",", u,") é uma cruzada")
    
    cor[s] = 'P'
    print("Tempo de fechamento do vertice ", s, " é ", t_atual)
    fecha[s] = t_atual
    t_atual = t_atual+1

def DFS(grafo):
   for i in range(6): 
        if(cor[i] == 'B'):
            DFS_VISIT(grafo, i)

g = criaGrafo()
DFS(g)

print(desc)
print(fecha)
print("csass")




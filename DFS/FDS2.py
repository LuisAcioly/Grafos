INFINITO = 1000000000

cor = ['B' for i in range(7)]
desc = [INFINITO for i in range(7)]
fech = [INFINITO for i in range(7)]

t_atual = 0

def criaGrafo():
    d = { 0 : [1, 2],
          1 : [3],
          2 : [2],
          3 : [2, 4, 5],
          4 : [5],
          5 : [],
          6 : [5],
        }
    return d

def DFS(grafo):
    for i in range(7):
        if(cor[i] == 'B'):
            DFS_Detec(grafo, i)


def DFS_Detec(grafo, s):
    global t_atual

    cor[s] = 'C'
    desc[s] = t_atual
    t_atual = t_atual+1


    for u in grafo[s]:
        if(cor[u] == 'B'):
            print("(", s, ",", u,") é um arco de arvore")
            cor[u] = 'C'
            desc[u] = t_atual
            DFS_Detec(grafo, u)
        elif(cor[u] == 'C'):
            print("(", s, ",", u,") é um arco de retorno")
            print("O grafo possui um ciclo")
        elif(cor[u] == 'P' and desc[s] < fech[u]):
            print("(", s, ",", u,") é um arco direto")
        else:
            print("(", s, ",", u,") é um arco cruzado")

    cor[s] = 'P'
    fech[s] = t_atual
    t_atual = t_atual+1
            
g = criaGrafo()
DFS(g)

print(cor)
print(desc)
print(fech)
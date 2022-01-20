t_atual = 0

g = {   0 : [1],
        1 : [2,3],
        2 : [4,5],
        3 : [4],
        4 : [6],
        5 : [6],
        6 : [],  
    }

def DFS_VISIT(grafo, s, f):
    global t_atual
    chaves = list(grafo.keys())
    cor = {}
    
    for i in range(len(chaves)):
        cor[chaves[i]] = 'B'

    for i in grafo[s]:
        if(f == i and cor[f] == 'B'):
            t_atual = t_atual + 1
        elif(cor[i] == 'B'):
            cor[i] = 'C'
            DFS_VISIT(grafo, i, f)
    cor[s] = 'P'


DFS_VISIT(g, 0, 4)
print(t_atual)
'''for i in range(6):
    for j in range(6):
        if(i != j):
            print("---------------" + str(i) + "-" + str(j) + "-----------")
            DFS(g, i, j)'''

grafo = {1: [2, 10],
         2: [3],
         3: [4],
         4: [5],
         5: [6],
         10 : [],
        }
cor = {}
pai = {}

for i in grafo:
    cor[i] = 'B'
    pai[i] = -1

conexo = True

Q = []

Q.append(1)
cor[1] = 'B'

while(Q != []):



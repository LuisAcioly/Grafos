N, M = input().split()

N = int(N)
M = int(M)

while(N > 0 and M > 0):
    if(5 <= N <= 500 and 5 <= M <= 500):
        labirinto = []
        for i in range(N):
            entrada =input()
            coluna = list(entrada)
            labirinto.append(coluna)

    N, M = input().split()

    N = int(N)
    M = int(M)
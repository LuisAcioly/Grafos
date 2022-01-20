lista_de_vertices = []
lista_de_arestas = []
instrucao = "vazio"
instrucaoNova = "vazio"
compila = 0
contador = 0


def colori_grafo(lista_de_vertices, lista_de_arestas):
    cores = {}
    compila = True
    aux = "null"

    for i in lista_de_arestas:
        if(aux == "null" and i[1] in lista_de_vertices):
            aux = i[0]
            cores[i[0]] = 'G'
            cores[i[1]] = 'B'
        elif(aux == i[0] and i[1] in lista_de_vertices):
            if(i[1] in cores):
                if(cores[i[1]] == 'R'):
                    compila = False
            else:
                cores[i[1]] = 'B'
            
            cores[aux] = 'R'
            aux = i[0]
        elif(i[1] in lista_de_vertices):
            cores[i[0]] = 'G'
            
            if(i[1] in lista_de_vertices):
                if(cores[i[1]] == 'R'):
                    compila = False
                else:
                    cores[i[1]] = 'B'
        else:
            compila = False

    if(compila):
        print("OK")
    else:
        print("Compilation error")
    return 0

while True and contador < 2000:
    try:
        instrucaoNova = input()

        contador = contador+1
        if(len(instrucaoNova) <= 10):
                if(len(instrucaoNova) == 6):
                    lista_de_vertices.append(instrucaoNova[0])
                    if(instrucao == "vazio"):
                        compila = compila + 1
                    elif(isinstance(instrucaoNova[0], str)):
                        if((instrucaoNova[5] in lista_de_vertices) == False):
                            compila = 0
                else:
                    if(compila == 2):
                        instrucao = instrucaoNova
                        lista_de_vertices.append(instrucaoNova[0])
                        lista_de_arestas.append((instrucaoNova[0], instrucaoNova[5]))
                        lista_de_arestas.append((instrucaoNova[0], instrucaoNova[9]))
                        if(isinstance(instrucaoNova[5], int)):
                            lista_de_vertices.append(instrucaoNova[5])
                        if(isinstance(instrucaoNova[9], int)):
                            lista_de_vertices.append(instrucaoNova[9])
    except EOFError:
        break

if(compila < 2):
    print("Compilation Error")
else:
    colori_grafo(lista_de_vertices, lista_de_arestas)
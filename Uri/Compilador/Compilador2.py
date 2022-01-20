lista_de_vertices = []
lista_de_arestas = []
instrucao = "vazio"
instrucaoNova = "vazio"
compila = 0
origens = []
contador = 0

def resposta(cores):
    cont = 0
    for i in cores:
        if(cores[i] == 'B'):
            cont = cont + 1
    if(cont == 3):
        print("OK")
    else:
        print("Compilation Error")
    
    return 0


def colori_grafo(lista_de_vertices, lista_de_arestas):
    cores = {}

    for i in grafo:
        cores[i] = 'B'
    cor = 'G'
    for j in lista_de_arestas:
        if(cor == 'G'):
            if(cores[j[1]] == 'G'):
                cores[j[0]] = 'R'
            else:
                cores[j[0]] = 'G'
                cor = 'R'
        else:
            if(cores[j[1]] == 'R'):
                cores[j[0]] = 'G'
            else:
                cores[j[0]] = 'R'
                cor = 'G'
    resposta(cores)
    return 0

while True and contador < 2000:
    try:
        instrucaoNova = input()

        contador = contador+1
        if(len(instrucaoNova) <= 10):
                if(len(instrucaoNova) == 6):
                    lista_de_vertices.append(instrucaoNova[0])
                    origens.append(instrucaoNova[0])
                    if(instrucao == "vazio"):
                        compila = compila + 1
                else:
 
                    if(instrucao == "vazio"):
                        instrucao = instrucaoNova
                        lista_de_vertices.append(instrucaoNova[0])
                    else:
                        lista_de_vertices.append(instrucaoNova[0])
                        lista_de_arestas.append((instrucao[0], instrucaoNova[0]))
                        if(instrucaoNova[5] != instrucao[5]):
                            lista_de_arestas.append((instrucao[5], instrucaoNova[5]))
                        elif(instrucaoNova[9] != instrucao[9]):
                            lista_de_arestas.append((instrucao[9], instrucaoNova[9]))
                        instrucao = instrucaoNova
    except EOFError:
        break

if(compila < 2):
    print("Compilation Error")
else:

    colori_grafo(grafo, lista_de_arestas)
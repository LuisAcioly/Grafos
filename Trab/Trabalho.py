INFINITO = 9999999999


arquivo = open("testes.txt.txt");

vertices = [[] for i in range(274) ]
cont =0
for i in range(31):
    cont+=1
    vert = arquivo.readline()
    print(vert,cont)
    vert = vert.split(",")
    
    a = int(vert[0])
    b = int(vert[1])
    
    
    vertices[a].append(b)
    vertices[b].append(a)

print(vertices)




def caixeiro(vertices , origem,destino):
    visitas = [ False for i in range(247)]
    Distancia_Maxima = 0
    while(visitas[destino] == False):
        visitas[origem] = True
        vizinhos = vertices[origem]
        menor_valor = INFINITO
        indice = INFINITO
        for i in range(len(vizinhos)):
            if menor_valor > vizinhos[i]:
                menor_valor = vizinhos[i]
                indice = i
        
        if(menor_valor != INFINITO):
            visitas[i] = True
            Distancia_Maxima = Distancia_Maxima + menor_valor
            origem = i
        menor_valor = INFINITO
        indice = INFINITO
    return Distancia_Maxima


print(caixeiro(vertices,5,10))









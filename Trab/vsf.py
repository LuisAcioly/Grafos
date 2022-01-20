def cria_grafo(listaDeInformações):
    testes = []

    for linha in listaDeInformações:
        dados = linha.split(",")
        palavra = str(dados[0]) + "," + str(dados[1])
        if(palavra in testes):
            print(palavra)
        else:
            testes.append(palavra)

    return 0

arquivo = open("testes3.txt.txt")
listaDeInformações = arquivo.readlines()

grafo = cria_grafo(listaDeInformações)
#Problema do Compilador - URI
#A ideia do exercicio é funcionar como um compilador , onde define-se uma instrução com
#dois registradores origens, um registrador destino e tambem as operacoes , o objetivo 
# e verificar se dado um numero x de instruções o programa compila

#Foi usado uma lista que armazena os registradores origem e a cada insercao verificava se 
# a instrução era valida


#--UFLA - Universidade Federal de Lavras--
#    Algoritimo em grafos
#    Professor Mayron César de O. Moreira.


#@author Luis Wagner Acioly Bastos 10A

#@author Walisson Mendes Ferreira 10A

#Lista que armazena os registradores de origem
origens = []
#Variavel que armazena o registrador destino temporario
temp = "vazio"
#Variavel que auxilia na contagem de 2000 instruções
contador = 0
#Variavel que verifica se as instruções compilam
compilou = True

#EOF
while True and contador < 2000:
    try:

        #É recebida a string da instrução
        instrucao = input()

        #A string é dividida em uma lista
        variaveis = instrucao.split()

        #Conta uma instrução lida
        contador = contador + 1

        #Como é aceito no maximo uma instrução do tipo "c := a + b" seu tamanho deve ser 
        #de no maximo 5
        if(len(variaveis) <= 5):
            #Instruções de tamanho 3 são instruções de origem, então o registrador é adicionado
            #a lista de origens
            if(len(variaveis) == 3):
                origens.append(variaveis[0])
            else:
                #Se a variavel temp for igual a "vazio" então ela é a primeira instrução
                if(temp == "vazio"):
                    #Temp recebe o registrador destino da instrução
                    temp = variaveis[0]
                    #Como é a primeira instrução deve se verificar se os registradores origens estão 
                    # na lista de origens, se não estiver o programa não compila
                    if((variaveis[2] in origens) == False or (variaveis[4] in origens) == False):
                        compilou = False
                
                #As demais instruções deve se verificar se os registradores origem são iguais a variavel temporaria
                # ou se estão na lista de origens, se não estiverem o programa não compila

                #Verifica o primeiro registrador origem esta na lista de origens
                elif(variaveis[2] != temp and (variaveis[2] in origens) == False):
                    compilou = False
                #Verifica o segundo registrador origem esta na lista de origens
                elif(variaveis[4] != temp and (variaveis[4] in origens) == False):
                    compilou = False
                #Se não  entrou em nenhuma condição, o programa compila então a variavel 
                # temp é atualizada
                else:
                    temp = variaveis[0]
        #Se a instrução tiver um tamanho maior que 5 então o programa não compila
        else:
            compilou = False

    except EOFError:
        break

#Imprimi se o programa compila
if(compilou):
    print("OK")
#Imprimi se o programa não compila
else:
    print("Compilation Error")
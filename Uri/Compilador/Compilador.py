erro = False
instrução = "vazio"
origens = "vazio"
contador = 0

while True and contador < 2000:
    try:
        instruçãoNova = input()
        
        if(len(instruçãoNova) <= 10):
            if(len(instruçãoNova) == 6):
                if(instrução == "vazio"):
                    instrução = instruçãoNova
                    origens = instruçãoNova[0]
                else:
                    if(instruçãoNova[5] in instrução):
                        instrução = instruçãoNova + origens
                    else:
                        instrução = instrução + instruçãoNova
                        origens = origens + instruçãoNova[0]
            elif(instruçãoNova[5] in instrução and instruçãoNova[9] in instrução):
                instrução = instruçãoNova + origens
            else:
                erro = True
        contador = contador + 1
    except EOFError:
        break

if(erro == False):
    print("OK")
else:
    print("Compilation Error")
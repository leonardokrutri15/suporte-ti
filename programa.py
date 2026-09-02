print("---"*10)
print("IT - SUPORTE")
print("---"*10)

from utils.itera import *

# Tela inicial

while True :
    valor=int(input("INICIAR DIAGNOSTICO [1]\nSAIR [2]\nDIGITE AQUI:"))

    limpar_tela()
    tempo()

    if valor == 1:
        print("iniciando diagnostico..")
        tempo()
        limpar_tela()

        while True:
            print("---"*10)
            print("MENU DE DIAGNOSTICOS")
            print("---"*10)

            menu=int(input("VERIFICAR :\n" 

            "CPU [1]\n" 
            "MEMORIA RAM [2]\n" 
            "DISCO [3]\n"
            "SISTEMA [4]\n" 
            "SAIR [5]\n"

            "DIGITE AQUI :"
            ))

            if menu==1:
                print("Verificando CPU")
                tempo()
                break

            elif menu==2:
                print("verificando memoria RAM")
                tempo()
                break

            elif menu ==3:
                print("verificando DISCO")
                tempo()
                break

            elif menu ==4 :
                print("verificando sistema")
                tempo()
                break
            
            elif menu ==5 :
                print("SAINDO..")
                tempo()
                break

            else:
                print("Valor não identificado , digite novamente")
        


    
        break

    elif valor == 2:
        print("saindo")
        tempo()
        break

    else:
        print("VALOR NÃO IDENTIFICADO , DIGITE NOVAMENTE")
        tempo()


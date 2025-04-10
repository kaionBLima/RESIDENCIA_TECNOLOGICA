vingadores = []
while True:
    vingador = input("Digite o nome dos vingadores que estavam em Guerra Ultimato: ")
    vingador = vingador.upper

    if vingador == "0":
        vingadores.remove("HOMEM DE FERRO")
        vingadores.remove("VIUVA NEGRA")
        break
    vingadores.append(vingador)
    print(vingadores)

#while True:
    #vingador = input("Quais herois você deseja remover? ")
    #if vingador != "0":
        #vingadores.remove(vingador)
    #else:
        #break
        
#print(vingadores)

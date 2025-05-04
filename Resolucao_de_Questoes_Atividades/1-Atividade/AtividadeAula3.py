# Questao 1:
# def minerar_carvao():
#     print("Você minerou carvão!")

# minerar_carvao()

#Questao 2:
# def minerar_mineral(mineral):
#     print(f'Voce minerou {mineral}')

# mine = input("Digite um mineral: ")
# minerar_mineral(mine)

# Questao 3:
# def coletar_item():
#     return "espada de ferro"

# var = coletar_item()
# print(var)

# Questao 4:
# def construir_porta(quantidade, bloco):
#     print(f'Você construiu uma porta com {quantidade} blocos de {bloco}')

# quant = int(input("Digite a quantidade de material usado para construir uma porta: "))
# bloc = input("Digite qual material da porta foi usado: ")
# construir_porta(quant, bloc)

# Questao 5:
# def derrotar_mob(tipo, nivel):
#     print(f"Tipo de mob: {tipo}")
#     print(f"Experiência adquirida após abater {tipo}: {nivel * 5}")

# varTipo = input("Qual o tipo do mob: ")
# varNivel = int(input("Qual a experiência adquirida: "))
# derrotar_mob(varTipo, varNivel)
    
# Questao 6:
# class Mob:
#     def __init__(self, nome, vida):
#         self.nome = nome
#         self.vida = vida

#     def mostrar_info(self):
#         print(f'O mob se chama {self.nome} e tem um tamanho total de {self.vida}')
    
# name = input("Nome do mob: ")
# vid = int(input("Vida igual a: "))

# mob = Mob(name, vid)
# mob.mostrar_info()

# Questao 7:
# class Creeper:
#     def __init__(self, vida):
#         self.vida = vida
    
#     def explodir(self):
#         print("BOOM! O Creeper explodiu!")

# mob = Creeper(30)
# mob.explodir()

# Questao 8:
# class Bloco:
#     def __init__(self, tipo, quebravel):
#         self.tipo = tipo
#         self.quebravel = quebravel

#     def quebrar(self):
#         if self.quebravel == 'Sim' or self.quebravel == 'sim':
#             print("Sim, é quebravel")
#         else:
#             print(f"{self.tipo} não é quebravel")


# tipoBloco = input("Que bloco quer saber o tipo? ")
# quebrar = input("É quebravel? ")
# bloco = Bloco(tipoBloco, quebrar)
# bloco.quebrar()

# Questao 9:
# class Jogador:
#     def __init__(self, vida, ataque):
#         self.vida = vida
#         self.ataque = ataque

#     def atacar(self, mob):
#         mob.vida -= self.ataque
#         print(f"O jogador atacou! Vida restante do mob: {mob.vida}")
    
# class Mob:
#     def __init__(self, vida):
#         self.vida = vida

#     def mostrar_vida(self):
#         print(f"A vida atual do mob é {self.vida}")

# vidaGamer = int(input("Digite a vida do jogador: "))
# vidaMob = int(input("Digite a vida do Mob: "))
# ataque = int(input("Qual o dano que o mob perderá? "))  

# gamer = Jogador(vidaGamer, ataque)
# mob = Mob(vidaMob)

# gamer.atacar(mob)
# mob.mostrar_vida()

# Questao 10:
class Inventario:
    def __init__(self):
        self.itens = []

    def adcionar_item(self):
        item = input("Diga o que queres adcionar: ")
        self.itens.append(item)

    def remover_item(self):
        item = input("O que queres remover do inventario? ")
        self.itens.remove(item)

    def mostrar_itens(self):
        print(f'Itens: {self.itens} \n')

print("Inventario de itens")
print("-------------------")
inventario = Inventario()

while True:
    dec = int(input("Escolha uma opcão: \n 1 - Adcionar itens: \n 2 - Remover itens \n 3 - Mostrar itens \n 4 - Sair do menu \n"))

    if dec == 1:
        quant = int(input("Quantos itens deseja adcionar? "))
        for i in range(quant):
            inventario.adcionar_item()

    elif dec == 2:
        inventario.mostrar_itens()
        inventario.remover_item()
    elif dec == 3:
        inventario.mostrar_itens()
    elif dec == 4:
        print('Saindo do menu.')
        break
    else:
        print("Não existe esta opcao. Digite uma acima!")

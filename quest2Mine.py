# #1
# def minerar_carvao():
#     print("Você minerou carvão!")

# minerar_carvao()   

#2
# def minerar(mineral):
#     print(f"Você minerou {mineral}!")

# minerar("diamante")

#3
# def coletar_item(item):
#     print(f"Coleta {item}")

# coletar_item("espada de ferro")

# #4
# def construir_porta(bloco, quantidade):
#     print(f"Você construiu uma porta com {quantidade} blocos de {bloco}")
#construir_porta()

# #5
# def derrotar_mob(tipo, nivel):
#     tipo = str(input("Digite o tipo de mob: "))
#     nivel = int(input("Digite o nível do mob"))
#     experiencia = nivel * 5

# #6
# class Mob:
#     def __init__(self, nome, vida):
#         self.nome = nome
#         self.vida = vida
    
#     def status(self):
#         print(self.nome)
#         print(self.vida)

# #7
# class Creeper:
#     def __init__(self, vida):
#         self.vida = vida

#     def explodir():
#         print("BOOM! O Creeper explodiu")
    
#     explodir()

# #8
# class Bloco:
#     def __init__(self, tipo, quebravel):
#         self.tipo = tipo
#         self.quebravel = quebravel

#     def quebrar(self):
#         if self.quebravel == True:
#             print("Bloco quebrado")
#         else:
#             print("Não quebrável")

#     quebrar()

#9 
# class Jogador:
#     def __init__(self, nome, dano):
#         self.nome = nome
#         self.dano = dano

#     def atacar(self):
#         return self.dano
        
# class Mob:
#     def __init__(self, nome, vida):
#         self.nome = nome
#         self.vida = vida

#     def perderVida(self, dano):
#         self.vida -= dano
#         if self.vida <= 0:
#             print("Morreu")
#         else:
#             print(f"Quantidade de vida: {self.vida}")

# branlim = Jogador("Branlim", 100)
# alde = Mob("Aldeão", 120)

# alde.perderVida(branlim.atacar())

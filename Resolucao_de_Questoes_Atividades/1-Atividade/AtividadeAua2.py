# Questao 1
# listaHerois = []

# print("Convocacão vingadores:")
# for i in range(3):
#     Herois = str(input(f'Digite o nome do {i+1}º heroi: '))
#     listaHerois.append(Herois)

# print("\n",listaHerois)

# Questao 2
# armadHfTupla = ('Mark 1', 'Mark 2', 'Mark 3', 'Mark 4', 'Mark 5')

# print(f'primeiraVersao = {armadHfTupla[0]}') 
# print(f'UltimaVersao = {armadHfTupla[4]}') 

# Questao 3
# listaDignos = ['Thor, Capitao , Visao']
# print("Voce tem 3 tentativas para descobrir os dignos do Mjonir")


# for i in range(3):
#     verifica = input(f'Digite sua {i+1}º tentativa: ')

#     if verifica == 'Thor' or verifica == 'Capitao' or verifica == 'Visao':
#         print('Voce acertou, parabens!')
#         break
#     else:
#         ("Tente novamente")

#  Questao 4:
# listaH = []

# for i in range(5):
#     name = input(f"Diga o nome do {i+1}º que deseja adcionar a lista: ").upper()
#     listaH.append(name)

# print(listaH)

#  Questao 5:
# pedraTupla = (3, 6, 9)

# a, b, c = pedraTupla
# media = (a + b + c) / 3
# print(media)

# Questao 6:
# cap = {"capita america", "falcao", "feiticeira", "homem formiga", "gaviao arqueiro", "soldado invernal", "viuva negra", "hulk", "doutor estranho"}
# homemferro = {"homem de ferro", "viuva negra", "maquina de combate", "visao", "pantera negra", "homem aranha", "hulk", "doutor estranho"}

# print("Estao nos dois lado: ", cap & homemferro)
# print("Estao em apenas um lado: ", cap - homemferro)

# Questao 7:
numeros_pares = 0
numeros_impares = 0
lista_numeros = []

print("Insira 6 números inteiros:")

for i in range(6):
  numero = int(input(f"Digite o {i+1}º número: "))
  lista_numeros.append(numero)

for numero in lista_numeros:
  if numero % 2 == 0:
    numeros_pares += 1
  else:
    numeros_impares += 1

print(f"Números digitados: {lista_numeros}")
print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")




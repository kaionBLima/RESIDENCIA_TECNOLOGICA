# questao 1
# valor = input("Digite um valor qualque (int, str, float, bool...): ")

# if valor.lower == 'true' or valor.lower == 'false':
#     print('valor booleano')
# elif valor.isdigit():
#     print('valor inteiro')
# elif valor.count(".") == 1 and valor.replace(".", "").isdigit:
#     print('Valor float')
# else:
#     print('Valor String')

# questao 2
# valor1 = int(input("Digite o valor 1: "))
# valor2 = int(input("Digite o valor 2: "))

# float(valor1)
# float(valor2)

# soma = valor1 + valor2
# print(soma)

# questao 3
# chavePortal = float(input("Digite um numero impar ou par: "))

# if chavePortal % 2 == 0:
#     print("Portal aberto: ", chavePortal)
# else:
#     print('Portal negado: ', chavePortal)

# Questao 4
# numEscada = int(input("Diga um numero para liberar a escada: "))

# for i in range(numEscada):
#     print(f'Escada {i}')

# count = 0
# while count <= numEscada:
#     print(f'Escada {count}')
#     count += 1

# Questao 5
# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))

# media = (n1 + n2 + n3) / 3

# if media >= 7:
#     print("Fogo aprovado")
# elif media >= 5:
#     print("Fogo em treinamento")
# else:
#     print("Fogo reprovado")

# Questao 6
# num = int(input("Digite um numero para vermos a sua tabuada de multipicação: "))

# for i in range(11):
#     print(f'{num} x {i} = ', num * i)

# Questao 7:
# num = float(input("Jogue um numero: "))
# soma = 0
# soma = soma + num

# while num != 0:
#     num = float(input("Jogue mais um: "))
#     soma = soma + num

# print("Soma das moedas do baú = ", soma) 

# Questao 8:
# num = int(input("Digite um numero para sabermos se ele multiplo de 3 ou não: "))
# i = 1
# for i in range(num):
#     if i % 3 == 0:
#         print(f"Multiplo de 3: {i}")

# Questao 9:
# opcao = int

# while opcao != 3:
#     print("Conselho dos 3 codigos ")        
#     print("----------------------")
#     print("1 - Diga: Olá conselho")        
#     print("2 - Informe um numero e mostre o triplo")        
#     print("3 - Sair do conselho")  
#     opcao = int(input("Ecolha uma das opçoes: "))
#     if opcao == 1 :
#         print("Olá conselho")
#     elif opcao == 2 :
#         num = float(input("Informe um numero e apresente o triplo dele: "))
#         triplo = num * 3
#         print(f"Triplo = {triplo}")
#     elif opcao == 3:
#         print("Saindo do conselho")
#         break
#     else:
#         print("Opcao inexistente, escolha outra: ")

# Questao 10:
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# n3 = int(input("Digite o 3º número: "))
# n4 = int(input("Digite o 4º número: "))
# n5 = int(input("Digite o 5º número: "))

# if n1 < n2 < n3 < n4 < n5:
#     print("Os números estão em ordem crescente.")

# elif n1 > n2 > n3 > n4 > n5:
#     print("Os números estão em ordem decrescente.")

# else:
#     print("Os números estão sem ordem definida.")

# Questao 11
num_secreto = 37
print("Advinhe qual num secreto que move a pedra mágica. Voce tem 5 chances!")

for i in range(5):
    num = int(input(f"Tentativa {i+1}º: "))

    if num < num_secreto:
        print("É um numero maior, digite novamente")
    elif num > num_secreto:
        print("É um numero menor")
    elif num == num_secreto:
        print(f"Voce acertou, parabéns! O numero era {num_secreto}")
        break
    else:
        print("Suas chances acabaram, você perdeu. Sinto muito!")


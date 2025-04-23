import numpy as np 

# finn = np.random.randint(1, 11, 5)
# jack = np.random.randint(1, 11, 5)

# a = finn * jack
# print(a)
# b = np.sum(finn)
# b2_ = np.sum(jack)
# print(b, b2_)

# c = np.mean(finn)
# c2 = np.mean(jack)
# print(c, c2)

#Codigo do Axis, seletor de linhas e colunas para usar com grande numero de dados

gritos_finn = np.random.randint(1, 101, 4)
gritos_princesa = np.random.randint(1, 101, 4)
gritos_jack = np.random.randint(1, 101, 4)
gritos_rei = np.random.randint(1, 101, 4)

print(gritos_finn)
print(gritos_princesa)
print(gritos_jack)
print(gritos_rei)

gritos_reino = np.concatenate((gritos_finn, gritos_princesa, gritos_jack, gritos_rei))
print("\n\n", gritos_reino)

primeiros_gritos = gritos_reino[:4] 
print("\n\n", primeiros_gritos)


gritos_jacks = gritos_reino[8:12]
print("\n\nGritos Jack \n\n", gritos_jacks)

soma_total = gritos_reino.sum()
print("\nSoma total dos gritos:", soma_total)

matriz = np.array([gritos_finn, gritos_princesa, gritos_jack, gritos_rei])

soma_colunas = matriz.sum(axis=0)
somas_personagens = matriz.sum(axis=1)

print("\nSoma por coluna:", soma_colunas)
print("\nSoma por personagem (linha):", somas_personagens)

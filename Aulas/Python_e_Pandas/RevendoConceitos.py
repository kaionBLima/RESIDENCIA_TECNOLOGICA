# Percorrendo a lista kmh com for
kmh = [40, 45, 55, 60, 67, 80, 100]
mph = []
for i in kmh:
  mph.append(i/1.61)
print(mph)

# Fazendo a mesma coisa agora usando a função map(), pois ela resume tudo em apenas umas linha de codigo:
mph2 = list(map(lambda x: x/1.61), kmh) #Na função map ele utiliza a função lambda para percorrer a lista kmh, onde a declaramos após a virgula
print(mph2)

#Entendendo sobre List comprehension: Forma concisa e eficiente de criar listas, de forma mais resumida
mmph3 = [x/1.61 for x in kmh] #Lê-se da direita para esquerda para entender melhor
#Para x dentro de kmh, percorra esta lista e divida os elementos por 1.61 e adcione a nova lista mph3
print(mph3)





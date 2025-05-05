import numpy as np
# Questao 1:
# array = np.arange(0, 10)
# print(array)

# Questao 2:
# arrayZ = np.zeros((3, 3))
# arryOne = np.ones((3, 3))
# print(arrayZ, "\n")
# print(arryOne)

# Queestao 3:
# arrayEsp = np.linspace(1, 3, 10)
# print(arrayEsp)

# Questao 4:
# arrayA = np.array([10, 20, 30])
# arrayB = np.array([40, 50, 60])

# a = arrayA + arrayB

# arrayB.sum()

# print("Soma dos dois array: ", a)
# print("Soma do novo array:", a.sum())
# print(arrayA.sum())
# print(arrayB.sum())

# Questao 5:
# array = np.random.rand(5, 5)

# print(array)

# Questao 6:
# array = np.arange(0, 9).reshape(3, 3) * 10

# print(array)

# Questao 7:
# array = np.random.rand(5, 5)
# matrizArred = np.round(array, 2)
# matrizNv = matrizArred[array > 0.5]
# print(matrizArred)

# Questao 8:
# matriz = np.arange(0, 20)
# print(matriz)
# print(matriz.mean())
# print(matriz.sum())
# print(matriz.std())

# Questao 9:
# matriz = np.arange(0, 15).reshape([3, 5])
# print(matriz)

# Questao 10:
# forca1 = np.random.randint(1, 11, 5)
# forca2 = np.random.randint(1, 11, 5)

# soma = forca1 + forca2
# print("Soma das duas forças: ", soma)
# print("soma de todos os elementos de força 1: ",forca1.sum())
# print("soma de todos os elementos de força 2:",forca2.sum())
# print("Media força 1: ",forca1.mean())
# print("Media força 2: ",forca2.mean())
# print("Media soma das forcas: ", soma.mean())

# Questao 11:
array = np.arange(0, 16).reshape([4, 4])
arraysum = array.sum()
mediaSegColum = array[1, :].mean()
resetArray = np.delete(array, 3, axis=0)

print(array)
print(arraysum)
print(mediaSegColum)
print(resetArray)
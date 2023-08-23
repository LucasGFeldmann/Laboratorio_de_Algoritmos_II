import random

matriz = []

for line in range(3):
    matriz.append([])
    for dado in range(3):
        matriz[line].append(random.randint(0,10))

print(matriz)

maioresNumerosDaLinha = []

maior = 0

for line in matriz:
    for column in range(len(line)):
        if line[column] > maior:
            maior = line[column]
    maioresNumerosDaLinha.append(maior)
    maior = 0

print(maioresNumerosDaLinha)

soma = 0

for x in maioresNumerosDaLinha:
    soma += x

print(soma)
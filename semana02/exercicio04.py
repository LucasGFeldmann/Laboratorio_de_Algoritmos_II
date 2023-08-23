import random

matriz = []
mediaLine = []

for line in range(3):
    matriz.append([])
    for dado in range(3):
        matriz[line].append(random.randint(0,10))

print(matriz)

for line in range(3):
    soma = 0
    for column in range(3):
        soma += matriz[line][column]
    media = soma / 3
    soma = 0
    print(f"Média {line + 1}º linha: {media}")
    mediaLine.append(media)

somaLinha = 0
for x in mediaLine:
    somaLinha += x

mediaTotal = somaLinha / 3

print("Media Total:",mediaTotal)
    
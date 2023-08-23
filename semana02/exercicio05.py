import random

matriz01 = []
mediaLine = []

for line in range(3):
    matriz01.append([])
    for dado in range(3):
        matriz01[line].append(random.randint(0,10))

print(matriz01)

matriz02 = []
mediaLine = []

for line in range(3):
    matriz02.append([])
    for dado in range(3):
        matriz02[line].append(random.randint(0,10))

print(matriz02)

matriz03 = []

for line in range(3):
    matriz03.append([])
    for dado in range(3):
        matriz03[line].append(matriz01[line][dado] + matriz02[line][dado])

print(matriz03)

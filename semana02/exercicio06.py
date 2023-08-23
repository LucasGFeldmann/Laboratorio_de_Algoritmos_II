#matriz = [[1,2,3],[2,4,5],[3,5,6]]
matriz = [[2,3,4],[3,5,6],[4,6,7]]
transposta = 0

for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        if matriz[line][column] == matriz[column][line]:
            transposta += 1

if len(matriz[column]) * len(matriz[line]) == transposta:
    print("Sim")
else:
    print("Não")
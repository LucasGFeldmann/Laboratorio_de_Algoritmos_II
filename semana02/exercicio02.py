import random
lista = []

for x in range(10):
    lista.append(random.randint(0, 5))

lista.sort()
listaTratada = list(lista)
teste = []

for x in range(len(lista) - 1):
    if lista[x] == lista[x + 1]:
        teste.append(lista[x])

for x in teste:
    listaTratada.remove(x)

print(lista)
print(listaTratada)
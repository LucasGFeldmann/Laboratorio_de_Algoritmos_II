lista = [1,2,3,4,5]
novaLista = []

contador = len(lista) - 1

while contador >= 0:
    novaLista.append(lista[contador])
    contador -= 1

print(novaLista)
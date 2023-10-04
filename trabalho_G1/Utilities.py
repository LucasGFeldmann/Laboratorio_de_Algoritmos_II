import os
import Historic

def cleanConsole():
    print("\n" * os.get_terminal_size().lines)

# Tratar inputs

def isIntValue(value):
    while True:
        try:
            value = int(value)
            return value
        except:
            value = input("[ERROR] Digite um número Inteiro: ")

def isFloatValue(value):
    while True:
        try:
            value = value.replace(",", ".")
            value = float(value)
            return value
        except:
            value = input("[ERROR] Digite um número: ")

#

def showAllProducts(stock):
    cleanConsole()
    print("----LISTA DE PRODUTOS----\n")
    for products in stock:
        print(products + "--------")
        for keys, values in stock[products].items():
            print(keys.capitalize() + ": ", values)
    input("\nClique no enter para prosseguir...")

def exitEcheck(repit, stock):
    opt = input("\n1 - Repetir Operação\n2 - Sair\nDigite: ")
    print()
    if opt == "1":
        if type(stock) is not tuple:
            repit(stock)
        else:
            value01 = stock[0]
            value02 = stock[1]
            repit(value01, value02)      
    elif opt == "2":
        return
    else:
        cleanConsole()
        print(f"[ERROR] '{opt}' não é uma opção valida!\n")
        exitEcheck(repit, stock)

def showProduct(stock, item):
    if item not in stock.keys():
        cleanConsole()
        print(f"[ERROR] '{item}' não existente na lista de produtos")
        exitEcheck(searchProduct, stock)
    else:
        print("\n---------" + item)
        for keys, values in stock[item].items():
            print(keys.capitalize() + ": ", values)
        Historic.checkSell(item)
        input("\nClique no enter para prosseguir...")

def searchProduct(stock):
    cleanConsole()
    print("----INFORMAÇÕES DE UM PRODUTO----\n")
    item = input("Buscar produto: ")
    showProduct(stock, item)



# Filtro de Categoria

def showFilter(listaFiltrada):
    for items in listaFiltrada:
        print(f"{items[0]}--------")
        for key, value in items[1].items():
            if "categoria" != key:
                print(f"{key.capitalize()}: {value}")
    input("\nClique no enter para prosseguir...")

def filterCategory(stock, category):
    listaFiltrada = []
    for items in stock.items():
        if category == items[1]["categoria"]:
            listaFiltrada.append(list(items))
    showFilter(listaFiltrada)

def categoryExists(stock):
    cleanConsole()
    print("----ITENS DA CATEGORIA----\n")
    category = input("Categoria: ")
    print()
    counter = 0
    for items in stock.items():
        if category == items[1]["categoria"]:
            counter = 1
    if counter == 1:
        filterCategory(stock, category)
    else:
        print("[ERROR] Categoria Inexistente!")
        exitEcheck(categoryExists, stock)

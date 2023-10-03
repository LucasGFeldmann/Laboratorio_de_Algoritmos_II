import os

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
    for products in stock:
        print("\n---------" + products)
        for keys, values in stock[products].items():
            print(keys.capitalize() + ": ", values)
    input("\nClique no enter para prosseguir...")
     
def showProduct(stock):
    item = input("Digite o Item que deseja buscar: ")
    if item not in stock.keys():
        cleanConsole()
        print(f"=> '{item}' não existente na lista de produtos...")
        showProduct(stock)
    else:
        print("\n---------" + item)
        for keys, values in stock[item].items():
            print(keys.capitalize() + ": ", values)
        
        input("\nClique no enter para prosseguir...")

def cleanConsole():
    print("\n" * os.get_terminal_size().lines)

# Filtro de Categoria

def categoryExists(stock):
    category = input("Digite a categoria que deseja Vizualizar: ")
    counter = 0
    for items in stock.items():
        if category == items[1]["category"]:
            counter = 1
    if counter == 1:
        filterCategory(stock, category)
    else:
        newValue = input("Categoria Inexistente! Digite Novamente a categoria: ")
        categoryExists(stock, newValue)

def filterCategory(stock, category):
    listaFiltrada = []
    for items in stock.items():
        if category == items[1]["category"]:
            listaFiltrada.append(list(items))
    showFilter(listaFiltrada)

def showFilter(listaFiltrada):
    for items in listaFiltrada:
        print(f"\n{items[0]} --------")
        for key, value in items[1].items():
            if "category" != key:
                print(key, value)
    input("\nClique no enter para prosseguir...")


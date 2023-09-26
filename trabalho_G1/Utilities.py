import os

stock = {
    "Caneta" : {
        "amount" : 5,
        "price" : 1.90,
        "category" : "Materiais Escolares"
    },
    "Caderno" : {
        "amount" : 10,
        "price" : 5.90,
        "category" : "Materiais Escolares"
    },

}

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
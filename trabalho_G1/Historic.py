stock = {}
operationHistoric = []

def showHistoric():
    for line in operationHistoric:
        for operation, product in line.items():
            print("\n",operation, "-------")
            for key, values in product.items():
                print(key)
                print(values)
    input("\nClique enter para prosseguir...")

def showSells():
    for line in operationHistoric:
        for operation, product in line.items():
            if operation == "venda":
                print("\n",operation, "-------")
                for key, values in product.items():
                    print(key)
                    print(values)
    input("\nClique enter para prosseguir...")

# Vendas de um unico Produto

def checkSell():
    items = input("Digite o produto que deseja ver suas vendas: ")
    for line in operationHistoric:
        for operation, product in line.items():
            if operation == "venda":
                for key in product.items():
                    if key[0] == items:
                        showSellProduct(product)
                    else:
                        print("Produto não encontrado")
                        checkSell()

def showSellProduct(product):
    listProduct = []
    for line in operationHistoric:
        for operation, product in line.items():
            if operation == "venda":
                for key in product.items():
                    listProduct.append(key)
    for items in listProduct:
        print("\n",items[0])     
        print(items[1])          
    input("\nClique enter para prosseguir...")

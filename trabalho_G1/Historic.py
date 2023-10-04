import Utilities
from Utilities import cleanConsole

stock = {}
operationHistoric = []

def showHistoric():
    for line in operationHistoric:
        for operation, product in line.items():
            for key, values in product.items():
                print(f"\n{operation.upper()} => {key}:")
                for x, y in values.items():
                    print(f"{x.capitalize()}: {y}")
    input("\nClique enter para prosseguir...")

def showSells():
    for line in operationHistoric:
        for operation, product in line.items():
            if operation == "venda":
                for key, values in product.items():
                    print(f"\n{operation.upper()} => {key}:")
                    for x, y in values.items():
                        print(f"{x.capitalize()}: {y}")
    input("\nClique enter para prosseguir...")

# Vendas de um unico Produto

def checkSell(search):
    print("\n----HISTORICO DE VENDAS----\n")
    for line in operationHistoric:
        for operation, product in line.items():
            if operation == "venda":
                for name, properties in product.items():
                    if name == search:
                        print(f"{properties['data']} => {properties['quantia']} unidades por R${properties['preco']} totalizando: {properties['total']}")


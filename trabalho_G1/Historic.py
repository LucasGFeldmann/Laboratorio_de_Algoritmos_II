import Utilities
from Utilities import cleanConsole

stock = {}
operationHistoric = [{'adicao': {'Caderno': {'quantia': 100, 'preco': 5.5, 'categoria': 'Material Escolar'}}}, {'adicao': {'Lapis': {'quantia': 50, 'preco': 1.5, 'categoria': 'Material Escolar'}}}, {'venda': {'Caderno': {'quantia': 10, 'preco': 5.5, 'total': 55.0, 'data': '10/04/23'}}}, {'venda': {'Caderno': {'quantia': 20, 'preco': 5.5, 'total': 110.0, 'data': '10/04/23'}}}, {'venda': {'Caderno': {'quantia': 30, 'preco': 5.5, 'total': 165.0, 'data': '10/04/23'}}}, {'venda': {'Caderno': {'quantia': 40, 'preco': 5.5, 'total': 220.0, 'data': '10/04/23'}}}, {'venda': {'Lapis': {'quantia': 25, 'preco': 1.5, 'total': 37.5, 'data': '10/04/23'}}}, {'venda': {'Lapis': {'quantia': 25, 'preco': 1.5, 'total': 37.5, 'data': '10/04/23'}}}]

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


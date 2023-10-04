import datetime
import Utilities

from Historic import operationHistoric
from Utilities import cleanConsole

def showSell(stock, product, amount):
    print("\nResumo da Venda\n")
    print(f"{product.capitalize()} => Quantia: {amount} => Preço Unitario: {stock[product]['preco']} => Total: {amount * stock[product]['preco']}")

def productAmount(stock, product):
    amount = Utilities.isIntValue(input("Digite a quantidade que deseja vender:"))
    if amount > stock[product]["quantia"]:
        cleanConsole()
        print("Quantia indisponivel! A disponibilidade atual é de:", stock[product]["quantia"])
        Utilities.exitEcheck(productAmount, (stock, product))
    else:
        operationHistoric.append({
        "venda" : {
            product : {
                "quantia" : amount,
                "preco" : stock[product]['preco'],
                "total" : amount * stock[product]['preco'],
                "data" : datetime.datetime.now().strftime("%x")}
            }
        })
        new_amount = stock[product]["quantia"] - amount
        stock[product].update({"quantia" : new_amount})
        showSell(stock, product, amount)
        input("\nDigite enter para continuar...")

def sellProduct(stock):
    cleanConsole()
    print("----VENDER PRODUTO----\n")
    item = input("Produto: ")
    if item not in stock.keys():
        print("[ERROR] Produto Inexistente!")
        Utilities.exitEcheck(sellProduct, stock)
    else:
        productAmount(stock, item)

from Historic import operationHistoric
import datetime

def showSell(stock, product, amount):
    print("\nResumo da Venda\n")
    print(f"{product.capitalize()} => Quantia: {amount} => Preço Unitario: {stock[product]['preco']} => Total: {amount * stock[product]['preco']}")

def productAmount(stock, product):
    amount = int(input("Digite a quantidade que deseja vender:"))
    if amount > stock[product]["quantia"]:
        print("Quantia indisponivel! A disponibilidade atual é de:", stock[product]["quantia"])
        productAmount(stock, product)
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
    item = input("Digite o produto que deseja veder: ")
    if item not in stock.keys():
        print("Produto Inexistente!")
        sellProduct(stock)
    else:
        productAmount(stock, item)

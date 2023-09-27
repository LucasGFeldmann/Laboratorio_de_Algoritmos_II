from Historic import operationHistoric
import datetime

def showSell(stock, product, amount):
    print("\nResumo da Venda\n")
    print(f"{product.capitalize()} => Quantia: {amount} => Preço Unitario: {stock[product]['price']} => Total: {amount * stock[product]['price']}")

def productAmount(stock, product):
    amount = int(input("Digite a quantidade que deseja vender:"))
    if amount > stock[product]["amount"]:
        print("Quantia indisponivel! A disponibilidade atual é de:", stock[product]["amount"])
        productAmount(stock, product)
    else:
        operationHistoric.append({
        "sellProduct" : {
            product : {
                "amount" : amount,
                "price" : stock[product]['price'],
                "total" : amount * stock[product]['price'],
                "date" : datetime.datetime.now().strftime("%x")}
            }
        })
        new_amount = stock[product]["amount"] - amount
        stock[product].update({"amount" : new_amount})
        showSell(stock, product, amount)
        input("\nDigite enter para continuar...")

def sellProduct(stock):
    item = input("Digite o produto que deseja veder: ")
    if item not in stock.keys():
        print("Produto Inexistente!")
        sellProduct(stock)
    else:
        productAmount(stock, item)

from Utilities import stock
import Utilities
from Historic import operationHistoric

# Adicionando Produto

def saveOldValues(stock, item):
    old_values = []
    for values in stock[item].items():
            old_values.append(values[1])

    amount = old_values[0]
    price = old_values[1]
    category = old_values[2]
    return amount, price, category

def addValues(amount, price, category, stock, item):
    stock[item] = {}
    stock[item] = {"amount" : amount}
    stock[item].update({"price" : price})
    stock[item].update({"category" : category})


def inputValues(stock, item):
    amount = int(input("Digite a quantia desse produto: "))
    price = float(input("Digite o preço desse produto: "))
    category = input("Digite a categoria desse produto: ")
    addValues(amount, price, category, stock, item)
    
    return amount, price, category

def sumValues(stock, item):
    old_amount, old_price, old_category = saveOldValues(stock, item)
    amount, price, category = inputValues(stock, item)

    final_amount = old_amount + amount
    final_price = old_price + price
    final_category = [old_category, category]

    operationHistoric.update({
        "sumValues" : {
            item : {
                "amount" : final_amount,
                "price" : final_price,
                "category" : final_category
            }
        }
    })

    addValues(final_amount, final_price, final_category, stock, item)

def addItem(stock):
    item = input("Digite o produto que deseja adicionar: ")
    if item in stock.keys():
        print("Item ja existente")
        sumValues(stock, item)
    else:
        amount, price, category = inputValues(stock, item)
        operationHistoric.update({
        "addItem" : {
            item : {
                "amount" : amount,
                "price" : price,
                "category" : category
            }
        }
    })

# Alterando Produto

def productChange(stock):
    item = input("Digite o nome do produto que deseja alterar os valores: ")
    if item in stock.keys():
        amount, price, category = inputValues(stock, item)
        operationHistoric.update({
        "productChange" : {
            item : {
                "amount" : amount,
                "price" : price,
                "category" : category
            }
        }
    })
    else:
        print("Produto não existente!")
        productChange(stock)

# Deletando Produto

def delProduct(stock):
    item = input("Digite o nome do produto que deseja deletar: ")
    if item in stock.keys():
        operationHistoric.update({
            "delProduct" : { item : stock[item]}
        })
        del stock[item]
    else:
        print("Produto não existente!")
        delProduct(stock)

delProduct(stock)
Utilities.showAllProducts(stock)
print(operationHistoric)
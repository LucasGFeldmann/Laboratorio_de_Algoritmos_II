from Historic import operationHistoric
import Utilities

from Utilities import cleanConsole

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
    stock[item] = {"quantia" : amount}
    stock[item].update({"preco" : price})
    stock[item].update({"categoria" : category})

def inputValues(stock, item):
    amount = Utilities.isIntValue(input("Quantia atual em estoque: "))
    price = Utilities.isFloatValue(input("Preço unitario: R$"))
    category = input("Qual a sua categoria: ")
    addValues(amount, price, category, stock, item)
    
    return amount, price, category

def sumValues(stock, item):
    old_amount, old_price, old_category = saveOldValues(stock, item)
    amount, price, category = inputValues(stock, item)

    final_amount = old_amount + amount
    final_price = old_price + price
    final_category = [old_category, category]

    operationHistoric.append({
        "soma" : {
            item : {
                "quantia" : final_amount,
                "preco" : final_price,
                "categoria" : final_category
            }
        }
    })

    addValues(final_amount, final_price, final_category, stock, item)

def addItem(stock):
    cleanConsole()
    print("----ADICIONANDO PRODUTO----\n")
    item = input("Nome produto: ")
    if item not in stock.keys():
        amount, price, category = inputValues(stock, item)
        operationHistoric.append({
        "adicao" : {
            item : {
                "quantia" : amount,
                "preco" : price,
                "categoria" : category
            }
        }
    })
    else:
        print("Item ja existente")
        sumValues(stock, item)
        
# Alterando Produto

def productChange(stock):
    item = input("Digite o nome do produto que deseja alterar os valores: ")
    if item in stock.keys():
        amount, price, category = inputValues(stock, item)
        operationHistoric.append({
        "alteracao" : {
            item : {
                "quantia" : amount,
                "preco" : price,
                "categoria" : category
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
        operationHistoric.append({
            "exclusao" : { item : stock[item]}
        })
        del stock[item]
    else:
        print("Produto não existente!")
        delProduct(stock)
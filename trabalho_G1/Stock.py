from Utilities import stock
import Utilities

def saveOldValues(stock, item):
    old_values = []
    for values in stock[item].items():
            old_values.append(values[1])
    return old_values

def addValues(amount, price, category, stock, item):
    stock[item] = {}
    stock[item] = {"amount" : amount}
    stock[item].update({"price" : price})
    stock[item].update({"category" : category + " "})


def inputValues(stock, item):
    amount = int(input("Digite a quantia desse produto: "))
    price = float(input("Digite o preço desse produto: "))
    category = input("Digite a categoria desse produto: ")
    addValues(amount, price, category, stock, item)
        
    new_values = [amount, price, category]
    
    return new_values

def sumValues(stock, item):
    final_value = []
    old_values = saveOldValues(stock, item)
    new_values = inputValues(stock, item)
    for x in range(len(old_values)):
        final_value.append(old_values[x] + new_values[x])

    amount = final_value[0]
    price = final_value[1]
    category = final_value[2]

    addValues(amount, price, category, stock, item)

def addItem(stock):
    item = input("Digite o produto que deseja adicionar: ")
    if item in stock.keys():
        print("Item ja existente")
        sumValues(stock, item)
    else:
        inputValues(stock, item)


addItem(stock)
print(stock)
Utilities.showAllProducts(stock)


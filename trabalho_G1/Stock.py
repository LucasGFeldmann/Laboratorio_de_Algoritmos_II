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
####

def intValues(value):
    try:
        value = int(value)
    except:
        value = input("Valor deve ser inteiro: ")
        intValues(value)
    else:
        print(type(value))
        return value

def floatValues(value):
    try:
        value = float(value)
    except:
        print("Só é permitido números com casa decimal dividida com '.'!")
        value = input("Digite novamente o valor: ")
        floatValues(value)
    value = float(value)
    return value

####
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

    operationHistoric.append({
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
        operationHistoric.append({
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
        operationHistoric.append({
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
        operationHistoric.append({
            "delProduct" : { item : stock[item]}
        })
        del stock[item]
    else:
        print("Produto não existente!")
        delProduct(stock)
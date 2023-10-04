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
    return amount, price

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
    amount = Utilities.isIntValue(input("Quantia a adicionar: "))
    price = Utilities.isFloatValue(input("Preço a adicionar: R$"))

    old_amount, old_price = saveOldValues(stock, item)

    final_amount = old_amount + amount
    final_price = old_price + price
    addValues(final_amount, final_price, stock[item]["categoria"], stock, item)

    operationHistoric.append({
        "soma" : {
            item : {
                "quantia" : f"{old_amount} + {amount} = {final_amount}",
                "preco" : f"{old_price} + {price} = {final_price}",
            }
        }
    })

def addToSum(stock, item):
    choice = Utilities.isIntValue(input("1 - Voltar para o menu\n2 - Adicionar mais valor\nDigite: "))
    if choice == 1:
        return
    elif choice == 2:
        cleanConsole()
        print("----ACRÉSCIMO DE VALOR----\n")
        Utilities.showProduct(stock, item)
        sumValues(stock, item)
    else:
        print(f"[ERROR] '{choice}' não é uma opção!")
        addToSum(stock, item)

#addToSum({}, "Caderno")

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
        print("\nProduto já cadastrado!\n")
        addToSum(stock, item)

# Alterando Produto

def productChange(stock):
    cleanConsole()
    print("----ALTERAÇÃO DE DADOS----\n")
    item = input("Produto: ")
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
        print("\n[ERROR] Produto não encontrado!")
        Utilities.exitEcheck(productChange, stock)


# Deletando Produto

def delProduct(stock):
    cleanConsole()
    print("----DELETAR PRODUTO----\n")
    item = input("Produto: ")
    if item in stock.keys():
        operationHistoric.append({
            "exclusao" : { item : stock[item]}
        })
        del stock[item]
        input(f"'{item}' - Deletado\n\nPressione enter para prosseguir...")
    else:
        print(f"\n[ERROR] '{item}' Inexistente!")
        Utilities.exitEcheck(delProduct, stock)
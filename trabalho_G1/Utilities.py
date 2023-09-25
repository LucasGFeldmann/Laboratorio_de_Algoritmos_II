stock = {
    "Caneta" : {
        "amount" : 5,
        "price" : 1.90,
        "category" : "Materiais Escolares "
    },
    "Caderno" : {
        "amount" : 10,
        "price" : 5.90,
        "category" : "Materiais Escolares "
    },

}

def showAllProducts(stock):
    for products in stock:
        print("\n---------" + products)
        for keys, values in stock[products].items():
            print(keys.capitalize() + ": ", values)

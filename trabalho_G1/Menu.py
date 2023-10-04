import Historic
import Utilities
import Stock
import Sales

from Utilities import cleanConsole
from Historic import stock

def salesMenu():
    opt = 0
    while opt != "7":
        
        print("----SEÇÃO VENDAS----\n")

        print("1 - Vender Produto")

        print("2 - Listar Todos Produtos")
        print("3 - Informação Produto + Historico de Vendas")
        print("4 - Exibir Produtos de uma Categoria")

        print("5 - Fechar Vendas")

        print()

        opt = input("Digite a opção que deseja realizar: ")

        if opt == "1":
            Sales.sellProduct(stock)
            cleanConsole()
        elif opt == "2":
            Utilities.showAllProducts(stock)
            cleanConsole()
        elif opt == "3":
            Utilities.searchProduct(stock)
            cleanConsole()
        elif opt == "4":
            Utilities.categoryExists(stock)
            cleanConsole()
        elif opt == "5":
            cleanConsole()
            startMenu()
        else:
            cleanConsole()
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            salesMenu()

def stockMenu():
    opt = 0
    while opt != "7":

        print("----SEÇÃO ESTOQUE----\n")

        print("1 - Adicionar Produto")
        print("2 - Excluir Produto ")
        print("3 - Alterar Dados Produto")

        print("4 - Listar Todos Produtos")
        print("5 - Informação Produto + Historico de Vendas")
        print("6 - Exibir Produtos de uma Categoria")

        print("7 - Fechar Estoque")

        print()

        opt = input("Digite a opção que deseja realizar: ")

        print("\n--------\n")
        
        if opt == "1":
            Stock.addItem(stock)
            cleanConsole()
        elif opt == "2":
            Stock.delProduct(stock)
            cleanConsole()
        elif opt == "3":
            Stock.productChange(stock)
            cleanConsole()
        elif opt == "4":
            Utilities.showAllProducts(stock)
            cleanConsole()
        elif opt == "5":
            Utilities.searchProduct(stock)
            cleanConsole()
        elif opt == "6":
            Utilities.categoryExists(stock)
            cleanConsole()
        elif opt == "7":
            cleanConsole()
            startMenu()
        else:
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            stockMenu()

def reportsMenu():
    opt = 0
    while opt != "10":
        
        print("----MENU DE RELATÓRIOS----\n")

        print("1 - Histórico Geral de Movimentações")
        print("2 - Historico de Vendas")
        print("3 - Informação Produto + Historico de Vendas")

        print("4 - Sair da aba de Relatórios")


        print()

        opt = input("Digite a opção a vizualizar: ")

        if opt == "1":
            cleanConsole()
            Historic.showHistoric()
            cleanConsole()
        elif opt == "2":
            cleanConsole()
            Historic.showSells()
            cleanConsole()
        elif opt == "3":
            cleanConsole()
            Utilities.searchProduct(stock)
            cleanConsole()
        elif opt == "4":
            cleanConsole()
            startMenu()
        else:
            cleanConsole()
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            reportsMenu()

def startMenu():
    opt = None
    while opt == None:
        
        print("----MENU PRINCIPAL----\n")

        print("1 - Seção Estoque")
        print("2 - Seção Vendas")
        print("3 - Seção Relatórios")

        print()

        opt = input("Digite a Seção que deseja Entrar: ")

        if opt == "1":
            cleanConsole()
            stockMenu()
        elif opt == "2":
            cleanConsole()
            salesMenu()
        elif opt == "3":
            cleanConsole()
            reportsMenu()
        else:
            cleanConsole()
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            startMenu()

cleanConsole()
startMenu()
import Historic
import Utilities
import Stock

from Stock import stock

def stockMenu():
    opt = 0
    while opt != "6":
        print("----SEÇÃO ESTOQUE----\n")

        print("1 - Adicionar Produto")
        print("2 - Alterar Dados Produto")
        print("3 - Excluir Produto")
        print("4 - Buscar Produto")
        print("5 - Listar Produtos")
        print("6 - Fechar Estoque")

        print()

        opt = input("Digite a opção que deseja realizar: ")

        print("\n--------\n")
        
        if opt == "1":
            Stock.addItem(stock)
            Utilities.cleanConsole()
        elif opt == "2":
            Stock.productChange(stock)
            Utilities.cleanConsole()
        elif opt == "3":
            Stock.delProduct(stock)
            Utilities.cleanConsole()
        elif opt == "4":
            Utilities.showProduct(stock)
            Utilities.cleanConsole()
        elif opt == "5":
            Utilities.showAllProducts(stock)
            Utilities.cleanConsole()
        elif opt == "6":
            Utilities.cleanConsole()
            startMenu()
        else:
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            stockMenu()

def reportsMenu():
    opt = 0
    while opt != "2":
        
        print("----MENU DE RELATÓRIOS----\n")

        print("1 - Histórico de Alterações")
        print("2 - Sair da aba de Relatórios")


        print()

        opt = input("Digite a opção a vizualizar: ")

        if opt == "1":
            Utilities.cleanConsole()
            Utilities.showAllProducts(Historic.operationHistoric)
            Utilities.cleanConsole()
        elif opt == "2":
            Utilities.cleanConsole()
            startMenu()
        else:
            Utilities.cleanConsole()
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            reportsMenu()

def startMenu():
    opt = 0
    while opt != "10":
        
        print("----MENU PRINCIPAL----\n")

        print("1 - Seção Estoque")
        print("2 - Seção Relatórios")

        print()

        opt = input("Digite a Seção que deseja Entrar: ")

        if opt == "1":
            Utilities.cleanConsole()
            stockMenu()
        elif opt == "2":
            Utilities.cleanConsole()
            reportsMenu()
        
        else:
            Utilities.cleanConsole()
            print(f"=> '{opt}' é uma Opção Ivalida!\n")
            startMenu()

Utilities.cleanConsole()
startMenu()



def salesMenu():
    pass





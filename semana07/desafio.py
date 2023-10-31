def input_float(value):
    while True:
        try:
            number = round(float(input(value).strip().replace(",",".")), 2)
            if number < 0:
                raise
            return number
        except:
            print("[ERROR] Digite um número valido!")


def deposit(account):
    depositValue = input_float("Valor deposito: R$")
    account["balance"] += depositValue
    account["historic"].append(f"Deposito: R${depositValue}")
    return account

def repit(operation, account):
    print("1 - Repetir Operação")
    print("2 - Voltar para o Menu")
    option = input("Opção: ")
    if option == "1":
        operation(account)
    elif option == "2":
        return
    else:
        input("[ERROR] Opção Invalida!")


def withdraw(account):
    withdrawValue = input_float("Valor saque: R$")
    if withdrawValue > account["balance"]:
        print("Valor maior que o saldo atual!")
        repit(withdraw, account)
    elif withdrawValue > account["transaction_limit"]:
        print("Limite de transação excedido!")
        repit(withdraw, account)
    else:
        print("opaaaaaa")
        account["balance"] -= withdrawValue
        account["historic"].append(f"Saque: R${withdrawValue}")
        return account
    return account

def check(account):
    print(f"Seu saldo atual é R${account["balance"]:.2f}")
    input("\nEnter para continuar ...")

def historic(account):
    for x in account["historic"]:
        print(x)
    input("\nEnter para continuar ...")

def menu(account):
    while True:
        print("\n" * 300)
        print("_________BANK_________")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Verificar Saldo")
        print("4 - Historico de Movimentações")
        print("5 - Sair")

        option = input("Digite sua opção: ")
        print()

        if option == "1":
            account = deposit(account)
        elif option == "2":
            account = withdraw(account)
        elif option == "3":
            check(account)
        elif option == "4":
            historic(account)
        elif option == "5":
            break
        else:
            print("[ERROR] Opção Invalida!")

def main():
    bank_account = {
        "balance": 0,
        "transaction_limit": 1000,
        "historic": []
    }
    menu(bank_account)

main()
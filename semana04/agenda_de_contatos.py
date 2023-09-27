def getPhones(contact_list):
    name = input("\nDigite o nome do contato:\n")
    print()
    if name not in contact_list.keys():
        print("Contato não encontrado!")
        getPhones(contact_list)
    else:
        for phone_number in contact_list[name]:
            print(phone_number)
    input("\npara proceguir precione enter...")

def addNumber(contact_list, name):
    yn = input(f"\nDigite o numero de {name}:\n")
    contact_list[name].append(yn)

def addOtherNumber(contact_list, name):
    result = 2
    while result != 0 and result != 1:
        result = int(input("\nVocê deseja adicionar outro número a esse contato?\nSe sim digite '1', se não digite '0'!\n"))
        if result == 1:
            addNumber(contact_list, name)
        elif result != 0 or result != 1:
            print("Verifique a opção!")

def createContact(contact_list):
    name = input("\nDigite o nome do Contato a ser adicionado:\n")
    contact_list[name] = []
    addNumber(contact_list, name)
    result = 1
    while result != 0:
        result = int(input("\nVocê deseja adicionar outro número a esse contato?\nSe sim digite '1', se não digite '0'!\n"))
        if result == 1:
            addNumber(contact_list, name)
        elif result != 0 and result != 1:
            print("Verifique a opção!")

def includePhone(contact_list):
    name = input("A qual contato deseja adicionar o Numero:\n")
    if name not in contact_list.keys():
        result = input("Contato não encontrado. Deseja adicionar? (S ou N)\n").upper()
        if result == "S":
            createContact(contact_list)
        elif result == "N":
            includePhone(contact_list)
        elif result != "N" or result != "S":
            print("Resposta não suportada!")
    else:
        value = input("Digite o número que deseja adicionar:\n")
        contact_list[name].append(value)

def choosingPhone(contact_list, name):
    for indexPhones in range(len(contact_list[name])):
        print((indexPhones + 1), "-", contact_list[name][indexPhones])
    delete = int(input("Digite a opção de número que deseja apagar: "))
    del contact_list[name][delete - 1]




def deletePhone(contact_list):
    name = input("\nDigite o nome do contato deseja deletar o número:\n")
    if name not in contact_list.keys():
        print("Contato não encontrado!")
        deletePhone(contact_list)
    elif len(contact_list[name]) == 1:
        del contact_list[name]
    else:
        choosingPhone(contact_list, name)

def deleteContact(contact_list):
    name = input("\nDigite o nome do contato deseja deletar:\n")
    if name not in contact_list.keys():
        print("Contato não encontrado!")
        deleteContact(contact_list)
    else:
        del contact_list[name]

def showList(contact_list):
    for name, phone in contact_list.items():
        print("\n" + name + ":")
        for x in phone:
            print("------- " + x)
    print(contact_list)
    input("\npara proceguir precione enter...")

def chooseOption():
    print("\n-----------------------------------------\n")
    print("1 - Encontrar telefone")
    print("2 - Criar contato")
    print("3 - Adicionar telefone")
    print("4 - Deletar contato")
    print("5 - Deletar telefone")
    print("6 - Apresentar lista de Contatos")
    print("7 - Sair")
    opt = int(input("\nDigite a sua opção: "))
    print("\n--------------------------")

    return opt

def optionSwitch(opt, contact_list):
    if opt == 1:
        getPhones(contact_list)
    elif opt == 2:
        createContact(contact_list)
    elif opt == 3:
        includePhone(contact_list)
    elif opt == 4:
        deleteContact(contact_list)
    elif opt == 5:
        deletePhone(contact_list)
    elif opt == 6:
        showList(contact_list)
    elif opt == 7:
        pass
    else:
        print("Invalid option!")

def main():
    contact_list = {}
    opt = 0
    while opt != 7:
        opt = chooseOption()
        optionSwitch(opt, contact_list)

main()
def print_list(shopping_list):
    print()
    for key, value in shopping_list.items():
        print(key.capitalize(), value + "x")

def request(shopping_list):
    amout_items = int(input("Quantos itens deseja adicionar? "))
    for x in range(amout_items):
        item = input("\nDigite o item: ")
        amount = input("Digite a quantia: ")
        shopping_list[item] = amount

def main():
    shopping_list = {}
    request(shopping_list)
    print_list(shopping_list)
    
main()
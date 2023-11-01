def find_element(list_element, index):
    if index < 0:
        raise IndexError("[ERROR] Não é permitido numero menor de 0")
    return list_element[index]

def main():
    try:
        list_element = [1,2,3,4,5,6,7,8,9]
        index = int(input("Digite o index que deseja acessar: "))
        result = find_element(list_element, index)
        print(result)
    except ValueError:
        print("[ERROR] Deve ser um numero")
    except IndexError:
        print("[ERROR] Index Inexistente")


main()
class NegativeNumberError(Exception):
     pass

def calculate_square_root(value):
    while True:
        try:
            number = float(input(value).strip().replace(",","."))
            if number < 0:
                raise NegativeNumberError
            result = number ** (1/2)
            return result, number
        except NegativeNumberError:
            print("A raiz quadrada de números negativos não é real.")
        except ValueError:
            print("[ERROR] Digite um número valido!")


def main():
    root, number = calculate_square_root("Digite o numero: ")
    print("A raiz de", number,"é:", root)

main()
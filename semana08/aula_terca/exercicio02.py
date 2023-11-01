def input_int(value):
    while True:
        try:
            number = int(input(value).strip())
            assert number >= 0 and number <= 10
            return number
        except:
            print("[ERROR] Digite um número valido!")


def main():
    value = input_int("Avalie com numero de 0 a 10: ")
    print("Sua avaliacao é", value)

main()
def input_float(value):
    while True:
        try:
            number = round(float(input(value).strip().replace(",",".")), 2)
            if number < 0:
                raise
            return number
        except:
            print("[ERROR] Digite um número valido!")

def validate(lado1, lado2, lado3, tipo):
    try:
        if lado1 + lado2 < lado3:
            raise ValueError
        else:
            return tipo
    except ValueError:
        print("NÃO É UM TRIANGULO")

def check(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        tipo = "Equilatero"
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        tipo = "Escaleno"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isoscele"
    if validate(lado1, lado2, lado3, tipo):
        return tipo

def main():
    lado1 = input_float("1 lado: ")
    lado2 = input_float("2 lado: ")
    lado3 = input_float("3 lado: ")
    
    tipo = check(lado1, lado2, lado3)
    if tipo:
        print("O triangulo é", tipo)

main()
def calculate(value):
    banknotes = []

    while value > 0:
        if value >= 100:
            value -= 100
            banknotes.append(100)
        elif value >= 50:
            value -= 50
            banknotes.append(50)
        elif value >= 20:
            value -= 20
            banknotes.append(20)
        elif value >= 10:
            value -= 10
            banknotes.append(10)

    print(f"{banknotes.count(100)} notas de R$ 100.00")
    print(f"{banknotes.count(50)} notas de R$ 50.00")
    print(f"{banknotes.count(20)} notas de R$ 20.00")
    print(f"{banknotes.count(10)} notas de R$ 10.00")


def main():
    value = int(input("Digite o valor: "))

    if value % 10 != 0:
        print("Valor inválido!")
    else:
        calculate(value)

main()
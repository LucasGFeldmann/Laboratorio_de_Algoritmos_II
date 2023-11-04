def read(text):
    file = open('exercicio02.txt', 'r')
    texto = file.readlines()
    line = 1
    for x in texto:
        line += 1
        if text.lower() in x.lower():
            print(f"linha: {line}\npalavra: {x}")




def main():
    print("\n" * 100)
    text = input("Digite a palavra que está procurando: ")
    print("\n--------------------------\n")
    read(text)

main()

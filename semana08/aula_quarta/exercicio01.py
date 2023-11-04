def read():
    file = open('exercicio01.txt')
    content = file.read().split(",")
    sum = 0
    for x in content:
        sum += int(x)
    print(sum / len(content))

read()
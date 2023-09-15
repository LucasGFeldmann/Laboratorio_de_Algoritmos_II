import random 

def generator(bingo_card):
    counter = 0
    while counter < 5:
        number = random.randint(0,99)
        if number not in bingo_card:
            bingo_card.append(number)
            counter += 1
    print(bingo_card)

def main():
    bingo_card = []
    generator(bingo_card)

main()

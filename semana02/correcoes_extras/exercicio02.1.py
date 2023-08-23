def sigle_list(primary_list):
    only_list = []
    for index in range(len(primary_list)):
        if primary_list[index] not in only_list:
            only_list.append(primary_list[index])
            print(only_list)

def main():
    primary_list = [0, 1, 2, 3, 3, 4, 4, 5, 5, 5]
    sigle_list(primary_list)

main()

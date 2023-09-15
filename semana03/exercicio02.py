import random
def print_matrix(matrix, range_matrix):
    for line in range(range_matrix):
        print(matrix[line])

def generator(matrix, range_matrix):
    for line in range(range_matrix):
        matrix.append([])
        for column in range(range_matrix):
            matrix[line].append(random.randint(0,10))

def sum_values(matrix, range_matrix):
    sum = 0
    for line in range(range_matrix):
        for column in range(range_matrix):
            if line > column:
                sum += matrix[line][column]
    return sum

def main():
    range_matrix = 3
    matrix = []

    generator(matrix, range_matrix)
    print_matrix(matrix, range_matrix)
    print(sum_values(matrix, range_matrix))

main()
import random

def different_directions(index_line, bigger_line, index_column, bigger_column, bigger_diagonal):
    if bigger_column > bigger_line:
        bigger = f"{index_column + 1}° column"
        if bigger_diagonal > bigger_column:
            bigger = "diagonal"
    elif bigger_line > bigger_diagonal:
        bigger = f"{index_line + 1}° line"
    else:
        bigger = "diagonal"

    print("The bigger is " + bigger)

def test_diagonal(matrix, range_matrix):
    product = 1
    for diaglonal in range(range_matrix):
        product *= matrix[diaglonal][diaglonal]

    return product


def test_column(matrix, range_matrix):
    for column in range(range_matrix):
        product = 1
        for line in range(range_matrix):
            product *= matrix[line][column]
        if column == 0:
            longest_product = product
            bigger = 0
        if longest_product < product:
            bigger = column
            longest_product = product

    return bigger, longest_product

def test_line(matrix, range_matrix):
    for line in range(range_matrix):
        product = 1
        for column in range(range_matrix):
            product *= matrix[line][column]
        if line == 0:
            longest_product = product
            bigger = 0
        if longest_product < product:
            bigger = line
            longest_product = product

    return bigger, longest_product

def print_matrix(matrix, range_matrix):
    for line in range(range_matrix):
        print(matrix[line])

def generator(matrix, range_matrix):
    for line in range(range_matrix):
        matrix.append([])
        for column in range(range_matrix):
            matrix[line].append(random.randint(1,2))

def main():
    matrix = []
    range_matrix = 5

    generator(matrix, range_matrix)
    print_matrix(matrix, range_matrix)
    index_line, bigger_line = test_line(matrix, range_matrix)
    index_column, bigger_column = test_column(matrix, range_matrix)
    bigger_diagonal = test_diagonal(matrix, range_matrix)
    different_directions(index_line, bigger_line, index_column, bigger_column, bigger_diagonal)


main()

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        for num in my_list:
            if num != my_list[0]:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print("")

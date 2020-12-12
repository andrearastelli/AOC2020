import os

from itertools import tee, accumulate
from operator import or_, and_
from pathlib import Path


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler.read().split("\n\n"):
            fields = row.split("\n")
            yield "".join(
                field
                for field in fields
                for key_value in field.split()
            )


def improved_load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler.read().split("\n\n"):
            fields = row.split("\n")
            yield [
                set(field)
                for field in fields
                for key_value in field.split()
            ]


def problem1(input_data):
    return map(len, map(list, map(set, input_data)))


def improved_problem1(input_data):
    return sum(map(len, [set.union(*data) for data in input_data]))


def problem2(input_data):
    return sum(map(len, [set.intersection(*data) for data in input_data]))


if __name__ == "__main__":
    input_data= load_data("./day06.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(sum(problem1(input_problem1)))

    #####

    input_data = improved_load_data("./day06.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(improved_problem1(input_problem1))
    print(problem2(input_problem2))

import os

from collections import Counter
from itertools import tee
from pathlib import Path


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler:
            yield row.strip()


def problem1(input_data):

    def guard_trees(input_tuple):
        idx, row = input_tuple

        return row[(idx * 3) % len(row)] == "#"

    filtered_result = filter(guard_trees, enumerate(input_data))

    return len(list(filtered_result))


if __name__ == "__main__":
    input_data = load_data("./day03.1.dat")

    input_problem1, input_problem2 = tee(input_data)

    print(problem1(input_problem1))


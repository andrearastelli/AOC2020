import math
import os

from functools import partial
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


def problem2(input_data):

    def guard_trees(input_tuple, col_step=1, row_step=1):
        idx, row = input_tuple

        return all([
            idx % row_step == 0,
            row[(idx * col_step) % len(row)] == "#"
        ])

    slope_functions = [
        partial(guard_trees, col_step=1, row_step=1),
        partial(guard_trees, col_step=3, row_step=1),
        partial(guard_trees, col_step=5, row_step=1),
        partial(guard_trees, col_step=7, row_step=1),
        partial(guard_trees, col_step=1, row_step=2)
    ]

    filtered_result = [
        filter(slope_fn, enumerate(input_data))
        for slope_fn, input_data in zip(slope_functions, tee(input_data, 5))
    ]

    return math.prod(list(map(len, map(list, filtered_result))))


if __name__ == "__main__":
    input_data = load_data("./day03.1.dat")

    input_problem1, input_problem2 = tee(input_data)

    print(problem1(input_problem1))
    print(problem2(input_problem2))


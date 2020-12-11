import math
import os

from itertools import tee, count, filterfalse
from operator import itemgetter
from pathlib import Path

def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler:
            yield row[:7], row[7:]


def bsp(val_set, min_val, max_val, guard_vals):
    low, high = min_val, max_val
    upper_guard, lower_guard = guard_vals
    for val in val_set:
        if val == upper_guard:
            low, high = (low + high) // 2 + 1, high
        elif val == lower_guard:
            low, high = low, (low + high) // 2

    return low


def problem1(input_data):
    for seats_col, seats_row in input_data:

        row_seats = bsp(seats_col, 0, 127, ("B", "F"))
        col_seats = bsp(seats_row, 0, 7, ("R", "L"))

        yield row_seats, col_seats, row_seats * 8 + col_seats


if __name__ == "__main__":
    input_data = load_data("./day05.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(max(problem1(input_problem1), key=itemgetter(2)))

    print(
        next(
            filterfalse(
                lambda x: x[0][2] == x[1],
                zip(
                    sorted(
                        problem1(input_problem2),
                        key=itemgetter(2)
                    ),
                    count(81)
                )
            )
        )
    )
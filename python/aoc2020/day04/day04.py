import math
import os

from itertools import tee
from pathlib import Path


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler.read().split("\n\n"):
            fields = row.split("\n")
            yield dict(
                key_value.split(":")
                for field in fields
                for key_value in field.split()
            )


def problem1(input_data):
    input_data1, input_data2 = tee(input_data, 2)

    # When all the keys are part of the dictionary, we can assume they are all valid
    only_full_fields = filter(lambda x: len(x) == 8, input_data1)

    partial_fields = filter(
        # Filter the sublist by retaining only the elements with no "cid" key in it
        lambda x: "cid" not in x,
        # Sublist containing only 7 keys
        filter(lambda x: len(x) == 7, input_data2)
    )

    return len(list(only_full_fields)) + len(list(partial_fields))


def problem2(input_data):
    return 0


if __name__ == "__main__":
    input_data = load_data("./day04.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(problem1(input_problem1))
    print(problem2(input_problem2))
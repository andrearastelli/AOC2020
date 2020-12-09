import math
import os

from itertools import combinations, tee
from pathlib import Path


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler:
            yield int(row)


def sum_mult_input_data(input_data, num_items):
    data_combinations = combinations(input_data, num_items)

    gate_sum_2020 = lambda x: sum(x) == 2020
    filtered_data = filter(gate_sum_2020, data_combinations)

    result = map(math.prod, filtered_data)

    return next(result)


if __name__ == "__main__":
    input_data = load_data("./day01.1.dat")

    part_1_input, part_2_input = tee(input_data, 2)

    part_1_result = sum_mult_input_data(part_1_input, 2)
    print(part_1_result)

    part_2_result = sum_mult_input_data(part_2_input, 3)
    print(part_2_result)


import os

from collections import Counter
from itertools import tee
from pathlib import Path

def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler:
            logic, password = row.split(": ")
            min_max, char = logic.split()
            char_min, char_max = min_max.split("-")

            yield int(char_min), int(char_max), char, password


def problem1(input_data):
    def password_guard(input_tuple):
        char_min, char_max, char, password = input_tuple
        pwd_counter = Counter(password)

        return pwd_counter[char] >= char_min and pwd_counter[char] <= char_max

    filtered_data = filter(password_guard, input_data)

    return len(list(filtered_data))


def problem2(input_data):
    def password_guard(input_tuple):
        pos_char_1, pos_char_2, char, password = input_tuple
        pos_char_1 -= 1
        pos_char_2 -= 1

        return bool(password[pos_char_1] == char) ^ bool(password[pos_char_2] == char)

    filtered_data = filter(password_guard, input_data)

    return len(list(filtered_data))


if __name__ == "__main__":
    input_data = load_data("./day02.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(problem1(input_problem1))

    print(problem2(input_problem2))
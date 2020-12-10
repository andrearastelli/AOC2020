import math
import os

from pathlib import Path


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        data_bucket = []
        for row in file_handler:
            data_row = row.strip()
            if data_row == "":
                yield dict(data.split(":") for data in data_bucket)
                data_bucket.clear()
            else:
                data_bucket.extend([data for data in data_row.split()])


if __name__ == "__main__":
    input_data = load_data("./day04.1.dat")

    def password_guard(input_data):
        valid_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        input_data_keys = set(input_data.keys())

        intersection_keys = valid_keys & input_data_keys

        return valid_keys == intersection_keys

    filtered_data = filter(password_guard, input_data)

    print(len(list(filtered_data)))


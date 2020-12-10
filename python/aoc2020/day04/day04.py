import math
import re
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
    filtered_data = filter(
        lambda x: len(x) == 8 or ("cid" not in x and len(x) == 7),
        input_data
    )

    return len(list(filtered_data))


def problem2(input_data):
    filtered_data = filter(
        lambda x: len(x) == 8 or ("cid" not in x and len(x) == 7),
        input_data
    )

    # BYR - Birth Year
    filtered_data = filter(lambda x: all([int(x["byr"]) >= 1920, int(x["byr"]) <= 2002]), filtered_data)

    # IYR = Issue Year
    filtered_data = filter(lambda x: all([int(x["iyr"]) >= 2010, int(x["iyr"]) <= 2020]), filtered_data)

    # EYR - Expiration Year
    filtered_data = filter(lambda x: all([int(x["eyr"]) >= 2020, int(x["eyr"]) <= 2030]), filtered_data)

    # HCL - Hair Color
    filtered_data = filter(lambda x: all([x["hcl"].startswith("#"), re.match(r"[0-9a-f]{6}", x["hcl"][1:])]), filtered_data)

    # PID - Passport ID
    filtered_data = filter(lambda x: all([len(x["pid"]) == 9, re.match(r"[0-9]{9}", x["pid"])]), filtered_data)

    # ECL - Eye Color
    filtered_data = filter(lambda x: x["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], filtered_data)

    def height_guard(height):
        if height.endswith("cm"):
            height = int(height.replace("cm", ""))
            return height >= 150 and height <= 193
        elif height.endswith("in"):
            height = int(height.replace("in", ""))
            return height >= 59 and height <= 76
        else:
            return False

    # HGT - Height
    filtered_data = filter(lambda x: height_guard(x["hgt"]), filtered_data)

    return len(list(filtered_data))


if __name__ == "__main__":
    input_data = load_data("./day04.1.dat")

    input_problem1, input_problem2 = tee(input_data, 2)

    print(problem1(input_problem1))
    print(problem2(input_problem2))
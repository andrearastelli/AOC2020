import os
import sys

from collections import defaultdict
from functools import partial
from pathlib import Path

p = partial(print, end="")


def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler:
            color, contents = [data.strip() for data in row.split("contain")]
            if contents == "no other bags.":
                contents = []
            else:
                contents = contents.split(", ")

            color = color.replace("bags", "").strip()
            contents = [
                (
                    int(content[:2]),
                    content[2:].replace("bags", "").replace("bag", "").strip(". ")
                )
                for content in contents
            ]
            yield color, contents


def bag_inspection(input_data: list, inspect_color: str, results: set):
    for bag, contents in input_data:
        contents = [content[1] for content in contents]
        if inspect_color in contents:
            results.add(bag)
            bag_inspection(input_data, bag, results)


def bag_count(input_data: list, inspect_color: str, number: int):
    result = number

    for bag, contents in input_data:

        if bag == inspect_color:

            if contents == []:
                return number

            sum_bag_numbers = 0
            for bag_number, contained_bag in contents:
                sum_bag_numbers += bag_count(input_data, contained_bag, bag_number)

            result = result + (number * sum_bag_numbers)

    return result



if __name__ == "__main__":

    input_data = load_data("day07.1.dat")

    input_data = list(input_data)

    results = set()
    checker = "shiny gold"

    bag_inspection(input_data, checker, results)
    print(len(results))

    number = 1
    number = bag_count(input_data, checker, number)
    print(number - 1)
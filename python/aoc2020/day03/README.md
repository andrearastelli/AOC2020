# Day 3

## Prompt 1

_With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees._

_Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:_

~~~
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
~~~
_These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:_

~~~
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
~~~

_You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map)._

_The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:_

_From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map._

_The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:_

~~~
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
~~~
_In this example, traversing the map using this slope would cause you to encounter 7 trees._

_Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?_

### Solution

Once found, the relationship between the row and the position on the row, the counting is pretty much straightforward to do.

~~~python
def problem1(input_data):

    def guard_trees(input_tuple):
        idx, row = input_tuple

        return row[(idx * 3) % len(row)] == "#"

    filtered_result = filter(guard_trees, enumerate(input_data))

    return len(list(filtered_result))
~~~

## Prompt 2

_Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all._

_Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:_

- _Right 1, down 1._
- _Right 3, down 1. **(This is the slope you already checked.)**_
- _Right 5, down 1._
- _Right 7, down 1._
- _Right 1, down 2._

_In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336._

_What do you get if you multiply together the number of trees encountered on each of the listed slopes?_

### Solution

This required a little bit of efforth to be solved.

The core of the problem is the logic to find the correct way to iterate thru the steps.

A guard function that returns `True` when the corresponding logic is verified is as follows:

~~~python
def guard_trees(input_tuple, col_step=1, row_step=1):
    idx, row = input_tuple

    return all([
        idx % row_step == 0,
        row[(idx * col_step) % len(row)] == "#"
    ])
~~~

Here the `col_step` and `row_step` needs to be updated to match all the different iterations required by the problem, and in order to fully embrace the functional side of the problem, i've thought of building a list of partial functions where the col and row steps are baked to match the input data, with a resulting function that looks like:

~~~python
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
~~~
# Day 5

## Prompt 1

_You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control._

_You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination._

_Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like `FBFBBFFRLR`, where `F` means "front", `B` means "back", `L` means "left", and `R` means "right"._

_The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row._

_For example, consider just the first seven characters of `FBFBBFFRLR`:_

- _Start by considering the whole range, rows 0 through 127._
- _`F` means to take the lower half, keeping rows 0 through 63._
- _`B` means to take the upper half, keeping rows 32 through 63._
- _`F` means to take the lower half, keeping rows 32 through 47._
- _`B` means to take the upper half, keeping rows 40 through 47._
- _`B` keeps rows 44 through 47._
- _`F` keeps rows 44 through 45._
- _The final `F` keeps the lower of the two, row 44._

_The last three characters will be either `L` or `R`; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half._

_For example, consider just the last 3 characters of `FBFBBFFRLR`:_

- _Start by considering the whole range, columns 0 through 7._
- _`R` means to take the upper half, keeping columns 4 through 7._
- _`L` means to take the lower half, keeping columns 4 through 5._
- _The final `R` keeps the upper of the two, column 5._

_So, decoding `FBFBBFFRLR` reveals that it is the seat at row 44, column 5._

_Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID `44 * 8 + 5 = 357`._

_Here are some other boarding passes:_

- _`BFFFBBFRRR`: row 70, column 7, seat ID 567._
- _`FFFBBBFRRR`: row 14, column 7, seat ID 119._
- _`BBFFBBFRLL`: row 102, column 4, seat ID 820._

_As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?_

### Solution 1

Binary space partitioning in a `val_set`, using a `min_val` and `max_val` as lower and upper bounds to be "partitioned", and `guard_vals` to use as flip/flop guards (must be a tuple of 2 elements, else everything fails and people will cry).

~~~python
def bsp(val_set, min_val, max_val, guard_vals):
    low, high = min_val, max_val
    upper_guard, lower_guard = guard_vals
    for val in val_set:
        if val == upper_guard:
            low, high = (low + high) // 2 + 1, high
        elif val == lower_guard:
            low, high = low, (low + high) // 2

    return low
~~~

Here... well.. we have to use `bsp()` twice, once for the rows between `0-127` and once for the columns between `0-7`.

As a nice plus, the function is a generator returning a tuple of 3 elements with row, column and the seat ID.

~~~python
def problem1(input_data):
    for seats_col, seats_row in input_data:

        row_seats = bsp(seats_col, 0, 127, ("B", "F"))
        col_seats = bsp(seats_row, 0, 7, ("R", "L"))

        yield row_seats, col_seats, row_seats * 8 + col_seats
~~~

To return the max seat ID, just use the max function over the 3rd value of the tuple in the list... yeee
~~~python
from operator import itemgetter

max(problem1(input_problem1), key=itemgetter(2))
~~~

## Prompt 2

_Ding! The "fasten seat belt" signs have turned on. Time to find your seat._

_It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well._

_Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list._

_What is the ID of your seat?_

### Solution 2

Given that the bulk of the work was already done in the first step, here I only needed to figure out how to extract the missing seat from the list.

So, sorting the list (and printing it) allows me to know that the lowest seat ID is 81 (and I don't really care about the highest).

Then, using a bunch of `itertools` functions, I've zipped the sorted list of tuples with the seat ID with a `itertools.counter` that starts at 81 (the lowest seat ID) and then with `itertools.filterfalse` filtered out the iterable by comparing the seat ID with the counter, and when they are not equal, just look for the first item as it'll contain the last element in the tuple with the correct seat ID.

~~~python
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
~~~

...if I would want to make this a little more readable (and possibly automatically valid for every version of this problem) I would do something like:

~~~python
sorted_input = sorted(problem1(input_problem2), key=itemgetter(2))
min_seat_id = min(sorted_input, key=itemgetter(2))
next(filterfalse(lambda x: x[0][2] == x[1], zip(sorted_input, count(min_seat_id)))
~~~
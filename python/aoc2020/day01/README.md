# Day 1

## Prompt 1

_Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up._

_Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together._

_For example, suppose your expense report contained the following:_

```
1721
979
366
299
675
1456
```

_In this list, the two entries that sum to **2020** are **1721** and **299**. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is **`514579`**._

_Of course, your expense report is much larger. Find the two entries that sum to **2020**; what do you get if you multiply them together?_

### Solution

First attempt to a solution, tuned to match the input data.

~~~python
data_combinations = combinations(input_data, 2)

gate_sum_2020 = lambda x: x[0] + x[1] == 2020

filtered_data = filter(gate_sum_2020, data_combinations)

gate_mult = lambda x: x[0] * x[1]

result = map(gate_mult, filtered_data)
~~~

## Prompt 2

_The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria._

_Using the above example again, the three entries that sum to **2020** are **979**, **366**, and **675**. Multiplying them together produces the answer, **241861950**._

_In your expense report, what is the product of the three entries that sum to **2020**?_

### Solution

Refined version of the previous solution with a more generic control over the input data.

Now this solution is generic enough to work with any combination of any number if elements from the input data, of which the sum adds up to 2020, and returning the product of those elements.

~~~python
def sum_mult_input_data(input_data, num_items):
    data_combinations = combinations(input_data, num_items)

    gate_sum_2020 = lambda x: sum(x) == 2020
    filtered_data = filter(gate_sum_2020, data_combinations)

    result = map(math.prod, filtered_data)

    return next(result)
~~~

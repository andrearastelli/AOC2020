# Day 6

## Prompt 1

_As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers._

_The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long._

_However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:_

    abcx
    abcy
    abcz

_In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)_

_Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:_

    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b

_This list represents answers from five groups:_

- _The first group contains one person who answered "yes" to 3 questions: a, b, and c._
- _The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c._
- _The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c._
- _The fourth group contains four people; combined, they answered "yes" to only 1 question, a._
- _The last group contains one person who answered "yes" to only 1 question, b._

_In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11._

_For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?_

### Solution 1

As for **DAY 04**, the key to this problem is the right formatting of the input data:

~~~python
def load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler.read().split("\n\n"):
            fields = row.split("\n")
            yield "".join(
                field
                for field in fields
                for key_value in field.split()
            )
~~~

Here I've joined together all the group of answers into a single string.

This because I could've then used the `set` to make unique values out of it to then count how many elements are in each set:


~~~python
def problem1(input_data):
    return map(len, map(list, map(set, input_data)))
~~~

## Prompt 2

_As you finish the last group's customs declaration, you notice that you misread one word in the instructions:_

_You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!_

_Using the same example as above:_

    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b

_This list represents answers from five groups:_

- _In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c._
- _In the second group, there is no question to which everyone answered "yes"._
- _In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count._
- _In the fourth group, everyone answered yes to only 1 question, a._
- _In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b._
_In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6._

_For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?_

### Solution 2

Ok, this will require an update in the parser for the input data:

~~~python
def improved_load_data(data_file):
    data_file_path = os.path.join(os.path.dirname(__file__), data_file)
    data_file = Path(data_file_path)

    with data_file.open("r") as file_handler:
        for row in file_handler.read().split("\n\n"):
            fields = row.split("\n")
            yield [
                set(field)
                for field in fields
                for key_value in field.split()
            ]
~~~

It now returns a list of sets, one set per person containing unique values for the answers.

This changes the solution to the first prompt in this way:
~~~python
def improved_problem1(input_data):
    return sum(map(len, [set.union(*data) for data in input_data]))
~~~

And this makes the solution for the second prompt pretty much straightforward, changing the union of the values to an intersection.
~~~python
def problem2(input_data):
    return sum(map(len, [set.intersection(*data) for data in input_data]))
~~~

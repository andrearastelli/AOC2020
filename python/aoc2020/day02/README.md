# Day 2

## Prompt 1

_Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan._

_The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look._

_Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen._

_To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set._

_For example, suppose you have the following list:_

~~~
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
~~~
_Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times._

_In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies._

_How many passwords are valid according to their policies?_

### Solution

Solution tuned for the problem.

~~~python
input_data = load_data("./day02.1.dat")

def password_guard(input_tuple):
    char_min, char_max, char, password = input_tuple
    pwd_counter = Counter(password)

    return pwd_counter[char] >= char_min and pwd_counter[char] <= char_max

filtered_data = filter(password_guard, input_data)

print(len(list(filtered_data)))
~~~

## Prompt 2

_While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting._

_The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently._

_Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement._

_Given the same example list from above:_

`1-3 a: abcde` _is valid: **position 1 contains a** and **position 3 does not.**_
`1-3 b: cdefg` _is invalid: neither position 1 nor position 3 contains b._
`2-9 c: ccccccccc` _is invalid: both position 2 and position 9 contain c._
_How many passwords are valid according to the new interpretation of the policies?_

### Solution

Given that the second part of the problem changes completely the rules of the first part, the new function has a completely different filter for the values in the input data.

~~~python
def problem2(input_data):
    def password_guard(input_tuple):
        pos_char_1, pos_char_2, char, password = input_tuple
        # Reset the indices as if they starts at 1 instead of 0
        pos_char_1 -= 1
        pos_char_2 -= 1

        # The two conditions needs to be exclusively true, so XOR it is
        return bool(password[pos_char_1] == char) ^ bool(password[pos_char_2] == char)

    filtered_data = filter(password_guard, input_data)

    return len(list(filtered_data))
~~~
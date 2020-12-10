# Day 4

## Prompt 1

_You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world._

_It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary._

_Due to some questionable network security, you realize you might be able to solve both of these problems at the same time._

_The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:_

~~~
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
~~~
_Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines._

_Here is an example batch file containing four passports:_

~~~
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
~~~
_The first passport is valid - all eight fields are present. The second passport is invalid - it is missing `hgt` (the Height field)._

_The third passport is interesting; the only missing field is `cid`, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing `cid` fields. Treat this "passport" as valid._

_The fourth passport is missing two fields, `cid` and `byr`. Missing `cid` is fine, but missing any other field is not, so this passport is invalid._

_According to the above rules, your improved system would report 2 valid passports._

_Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?_

### Solution 1

First step here is to have a well organized input data:

~~~python
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
~~~

and with this, we can evaluate the correctness of the fields by doing:

~~~python
def problem1(input_data):
    filtered_data = filter(
        lambda x: len(x) == 8 or ("cid" not in x and len(x) == 7),
        input_data
    )

    return len(list(filtered_data))
~~~

## Prompt 2

_The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!_

_You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:_

- `byr` _(Birth Year) - four digits; at least 1920 and at most 2002._
- `iyr` _(Issue Year) - four digits; at least 2010 and at most 2020._
- `eyr` _(Expiration Year) - four digits; at least 2020 and at most 2030._
- `hgt` _(Height) - a number followed by either cm or in:_
  - _If `cm`, the number must be at least 150 and at most 193._
  - _If `in`, the number must be at least 59 and at most 76._
- `hcl` _(Hair Color) - a # followed by exactly six characters 0-9 or a-f._
- `ecl` _(Eye Color) - exactly one of: amb blu brn gry grn hzl oth._
- `pid` _(Passport ID) - a nine-digit number, including leading zeroes._
- `cid` _(Country ID) - ignored, missing or not._

_Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:_

~~~
byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
~~~

_Here are some invalid passports:_

~~~
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
~~~

_Here are some valid passports:_

~~~
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
~~~

_Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?_

### Solution 2

..why keep things simple?

So I went a little overboard with this one. Just a bit.

~~~python
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
~~~
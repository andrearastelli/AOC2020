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
        data_bucket = []
        for row in file_handler:
            data_row = row.strip()
            if data_row == "":
                yield dict(data.split(":") for data in data_bucket)
                data_bucket.clear()
            else:
                data_bucket.extend([data for data in data_row.split()])
~~~

and with this, we can evaluate the correctness of the fields by doing:

~~~python
def password_guard(input_data):
    valid_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    input_data_keys = set(input_data.keys())

    intersection_keys = valid_keys & input_data_keys

    return valid_keys == intersection_keys

filtered_data = filter(password_guard, input_data)

print(len(list(filtered_data)))
~~~

## Prompt 2



### Solution 2
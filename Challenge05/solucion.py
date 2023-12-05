import re

file = open("database_attacked.txt", mode="rt")
data = file.read()

data_formatted = data.split("\n");
result = ""

def is_valid(entry_id, username, email, age, location):
    valid_id = re.compile(r"^[0-9a-zA-Z]+$")
    valid_username = re.compile(r"^[0-9a-zA-Z]+$")
    valid_email = re.compile(r"^[A-Za-z0-9]+@[a-z]+\.[a-z]+$")
    valid_age= re.compile(r"^\d+$")

    return  (re.match(valid_id, entry_id)
            and re.match(valid_username, username)
            and re.match(valid_email, email)
            and (age == "" or re.match(valid_age, age))
            and (location == "" or isinstance(location, str)))

for line in data_formatted:
    entry_id, username, email, age, location = line.split(",")
    validate_data = is_valid(entry_id, username, email, age, location)
    if not validate_data:
      result += username[0]

print(result)
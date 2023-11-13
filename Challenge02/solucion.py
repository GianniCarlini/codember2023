file = open("message_02.txt", mode="r")
data = file.read()

result = ""
accumulator = 0

for char in data:
    if char == "#":
        accumulator += 1
    elif char == "@":
        accumulator -= 1
    elif char == "*":
        accumulator *= accumulator
    elif char == "&":
        result += str(accumulator)

print(result)
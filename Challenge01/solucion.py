file = open("message_01.txt", mode="r")
data = file.read()

splitData = data.rstrip('\n').split()
counter = {}

for animal in splitData:
    if animal not in counter:
        counter[animal] = 0
    counter[animal] += 1

res = ''
for animalType, total in counter.items():
    res += animalType + str(total)
print(res)
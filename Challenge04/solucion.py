file = open("files_quarantine.txt", mode="rt")
data = file.read()

data_formatted = data.split("\n");
checked_files = []

for line in data_formatted:
    chain, checksum = line.split("-")

    check = ""
    for letra in chain:
      total = chain.count(letra)

      if (total == 1):
        check += letra

    if (check == checksum):
      checked_files.append(checksum)

    if len(checked_files) > 32:
        print(checked_files[32])
        break 
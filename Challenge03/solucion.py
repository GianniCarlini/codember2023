file = open("encryption_policies.txt", mode="rt")
data = file.read().strip()

result = 0
data_formatted = data.split("\n");
for line in data_formatted:
    policy, password = line.split(":")
    policy, letter = policy.split(" "); 
    min, max = policy.split("-"); 
    count = password.count(letter)
    if count < int(min) or count > int(max):
         result+=1

    if result == 42:
        print(password)
        break 
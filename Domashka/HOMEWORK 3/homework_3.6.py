total = 1

for i in range(1, 6):
    total = total * i
    for j in range(1, 6):
        multiplication = j * i
        print(f"{i} * {j} = {multiplication}")
print (total)
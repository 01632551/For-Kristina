firstRange = int(input())
secondRange = int(input())
counter = 0
for i in range(firstRange, secondRange + 1):
    for j in range(2, i + 1):
        if j != i and i % j == 0:
            counter += 1
    if counter == 0:
        print(i)
    counter = 0

for i in range(firstRange, secondRange + 1):
    for j in range(2, i + 1):
        if j != i and i % j == 0:
            break
    else: print(i)


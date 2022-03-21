num = int(input())
boardOfRange = 1
for i in range(1, num + 1):
    for j in range(boardOfRange, i + 1):
        print(str(i) * j)
    boardOfRange += 1
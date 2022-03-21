num = int(input())
sum = 0
factorial = 1
for i in range(1, num + 1):
    for j in range(1, i + 1):
        factorial *= j
    sum += factorial
    factorial = 1
print(sum)
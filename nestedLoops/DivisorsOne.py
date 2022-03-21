num1 = int(input())
num2 = int(input())
counter = 0
maxSumDivisors = 0
maxNumber = 0
for i in range(num1, num2 + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += j
    if counter > maxSumDivisors:
        maxSumDivisors = counter
        maxNumber = i
    counter = 0
print(maxNumber, maxSumDivisors)
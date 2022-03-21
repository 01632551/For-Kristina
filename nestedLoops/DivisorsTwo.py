num = int(input())
divisors = 0
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            divisors += 1
    print(i, '+' * divisors, sep='')
    divisors = 0
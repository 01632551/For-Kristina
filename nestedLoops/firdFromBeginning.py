num = int(input())
counter = 0
while num > 1000:
    num //= 10
print(num % 10)
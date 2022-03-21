num = int(input())
counterOfThreeOnes = 0
counterOfLastDigit = 0
counterOfEvenDigits = 0
sumOfOverFive = 0
multiplyOfOverSeven = 1
counterOfZeroAndFive = 0
lastDigit = num % 10
while num > 0:
    digit = num % 10
    if digit == 3:
        counterOfThreeOnes += 1
    if digit == lastDigit:
        counterOfLastDigit += 1
    if digit % 2 == 0:
        counterOfEvenDigits += 1
    if digit > 5:
        sumOfOverFive += digit
    if digit > 7:
        multiplyOfOverSeven *= digit
    if digit == 0 or digit == 5:
        counterOfZeroAndFive += 1
    num //= 10

print(counterOfThreeOnes, counterOfLastDigit, counterOfEvenDigits, sumOfOverFive, multiplyOfOverSeven, counterOfZeroAndFive, sep='\n')
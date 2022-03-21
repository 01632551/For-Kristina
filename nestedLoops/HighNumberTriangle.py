num = int(input())
num2 = int(input())
numberOfTriangle = 1
triangle = ''
index = 1
while numberOfTriangle <= num2:
    for j in range(1, index + 1):
        if numberOfTriangle > num2:
            break
        triangle += str(numberOfTriangle) + ' '
        numberOfTriangle += 1

    print(triangle)
    triangle = ''
    if numberOfTriangle > num2:
        break
    index += 1
    if index == num:
        while index != 1:
            for j in range(1, index + 1):
                if numberOfTriangle == num2:
                    break
                triangle += str(numberOfTriangle) + ' '
                numberOfTriangle += 1

            print(triangle)
            triangle = ''
            if numberOfTriangle > num2:
                break
            index -= 1

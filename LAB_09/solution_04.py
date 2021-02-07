import random as r

numbers = [r.randint(1,20) for x in range(15)] 

print(numbers)

def removeMin(numbers):
    numberTwo = numbers.copy()
    numberTwo.sort()
    minNumber = numberTwo.pop(0)
    i = 0
    while i < len(numbers):
        if numbers[i] == minNumber:
            numbers.pop(i)
            i == len(numbers)
        else:
            i += 1
    return numbers

print(removeMin(numbers))

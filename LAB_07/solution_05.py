import random

rangeOfNumber = 20

listOfNumbers = list()

for i in range(rangeOfNumber):
    listOfNumbers.append(random.randint(0, 99))
    
print(listOfNumbers)

listOfNumbers.sort()

print(listOfNumbers)
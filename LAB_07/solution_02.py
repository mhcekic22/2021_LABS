import random

randomRange = random.randint(0, 15)

randomNumberList = list()

resultPositive = 0
resultNegative = 0

for i in range(randomRange):
    randomNumberList.append(random.randint(0, 16))
    if i % 2 == 0 and i != randomRange-1: 
        randomNumberList.append("-")
    elif i % 2 == 1 and i != randomRange-1:
        randomNumberList.append("+")
for i in range(len(randomNumberList)):
    if i % 4 == 0:
        resultPositive += randomNumberList[i]
    elif i % 2 == 0:
        resultNegative += randomNumberList[i]

randomNumberListString = map(str, randomNumberList)

randomNumberListStringWord = " ".join(randomNumberListString)

print(randomNumberListStringWord, "=", (resultPositive - resultNegative))
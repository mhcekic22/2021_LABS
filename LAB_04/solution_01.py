numArray = list()
numArrayOdd = list()
numArrayEven = list()
numArrayCummulative = list()
numArrayNonDuplicate = list()

num = input("Enter how many elements you want:")

sum = 0

for i in range(int(num)):
    n = input("Enter the %d. :" % (i+1))
    numArray.append(int(n))
    if int(n) % 2 == 0:
        numArrayEven.append(int(n))
    else:
        numArrayOdd.append(int(n))
    sum = sum + int(n)
    numArrayCummulative.append(sum)
    
for i in range(len(numArray)):
    k = i+1
    for j in range(k, len(numArray)):
        if numArray[i] == numArray[j] not in numArrayNonDuplicate:
            numArrayNonDuplicate.append(numArray[i])

print("Array: ", numArray)

print("The min is: ", min(numArray))

print("The max is: ", max(numArray))

print("The even numbers are: ", numArrayEven)

print("The odd numbers are: ", numArrayOdd)

print("The cummulative sequence is: ", numArrayCummulative)

print("The only dublicate sequence is: ", numArrayNonDuplicate)



import random
array = list()
even = list()
equalValue = list()
reverseArray = list()

for i in range(11):
    array.append(random.randint(0, 9))

for i in range(len(array)):
    reverseArray.append(array[-(i+1)])
    if array[i] % 2 == 0:
        even.append(array[i])

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] == array[j] not in equalValue:
            equalValue.append(array[i])

print("All elements: ", array)
print("All elements of even index: ", even)
print("All elements of equal value: ", equalValue)
print("All elements of reverse order: ", reverseArray)
print("The first: ", array[0], "The second: ", array[-1])

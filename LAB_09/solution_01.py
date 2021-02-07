import random as r

rangeOfList = r.randint(10, 20)

NUMBER_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 10]

def swap(numbers): # TODO: swap first and the last number
    holder = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = holder
    return numbers

def shift(numbers): # TODO: shift all number by one and the last one to first
    holderList = swap(numbers = numbers.copy())
    for i in range(0, len(numbers) - 1):
        holderList[i+1] = numbers[i] 
    return holderList
        

def replace(numbers): # TODO: replace all elements with zero
    for i in range(len(numbers)):
        numbers[i] = 0
    return numbers
    

def replace2(numbers): # TODO: replace each element except the first and the last by the larger of its two neighbors
    holder = 0
    for i in range(1, len(numbers) - 1):
        if i == 1:
            if numbers[i + 1] > numbers[i]:
                holder = numbers[i + 1]
                numbers[i + 1] = numbers[i]
                numbers[i] = holder
                holder = 0
        elif i == len(numbers) - 2:
            if numbers[i - 1] > numbers[i]:
                holder = numbers[i - 1]
                numbers[i - 1] = numbers[i]
                numbers[i] = holder
                holder = 0
        else:
            if numbers[i - 1] > numbers[i + 1] and numbers[i - 1] > numbers[i]:
                holder = numbers[i - 1]
                numbers[i - 1] = numbers[i]
                numbers[i] = holder
                holder = 0
            elif numbers[i - 1] < numbers[i + 1] and numbers[i - 1] > numbers[i]:
                holder = numbers[i + 1]
                numbers[i + 1] = numbers[i]
                numbers[i] = holder
                holder = 0
    return numbers

def remove(numbers): # TODO: if len(numbers) = odd remove the middle, if len(numbers) = even remove the middle two numbers
    if len(numbers) % 2 == 0:
        lengthOfNumbers = int(len(numbers) / 2)
        numbers[lengthOfNumbers] = 0
        numbers[lengthOfNumbers - 1] = 0
    else:
        numbers[len(numbers) // 2] = 0
    return numbers


def move(numbers): # TODO: move all even elements to the front, preserving the orders of elements
    evenNumbers = list()
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            evenNumbers.append(numbers[i])
            numbers.pop(i)
        else:
            i += 1
    evenNumbers.sort()
    
    for i in range(len(evenNumbers)):
        numbers.insert(i, evenNumbers[i])
    
    return numbers


def returnLargest(numbers): # TODO: return the second largest element of the list
    maxNumber = max(numbers)
    i = 0 
    while i < len(numbers):
        if maxNumber == numbers[i]:
            numbers.pop(i)
        else:
            i += 1
    secondMaxNumber = max(numbers)
    return secondMaxNumber

def sortings(numbers): # TODO: if list is increasing order
    sortedList = numbers.copy()
    sortedList.sort()
    flag = 1
    
    for i in range(len(numbers)):
        if sortedList[i] != numbers[i]:
            flag = 0
    if flag == 1:
        return True
    else:
        return False
    
def duplicateTwoElementsAdjacent(numbers): # TODO: if list contains two adjacent duplicate elements
    flag = 0
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            flag = 1
    if flag == 1:
        return "There are two adjacent elements which are duplicates"
    else:
        return "There no adjacent duplicates"
    
def duplicateTwoElements(numbers): # TODO: if list has contais duplicate elements
    flag = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                flag = 1
    if flag == 1:
        return "The list contains duplicates"
    else:
        return "The list doesnt contain duplicates"



print(f"The real list is: {NUMBER_LIST}")
print(f"The swap function is: {swap(numbers = NUMBER_LIST.copy())}")
print(f"The shift function is: {shift(numbers = NUMBER_LIST.copy())}")
print(f"The replace function is: {replace(numbers = NUMBER_LIST.copy())}")
print(f"The replace2 function is: {replace2(numbers = NUMBER_LIST.copy())}")
print(f"The remove function is: {remove(numbers = NUMBER_LIST.copy())}")
print(f"the move function is: {move(numbers = NUMBER_LIST.copy())}")
print(f"The second max number is: {returnLargest(numbers = NUMBER_LIST.copy())}")
print(f"The sortings function is: {sortings(numbers = NUMBER_LIST.copy())}")
print(f"The duplicateTwoElementsAdjacent function is: {duplicateTwoElementsAdjacent(numbers = NUMBER_LIST.copy())}")
print(f"The duplicateTwoElements function is: {duplicateTwoElements(numbers = NUMBER_LIST.copy())}")

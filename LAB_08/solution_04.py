import random as r

rangeOfListsOne = r.randint(5, 10)
rangeOfListsTwo = r.randint(5, 10)

listOne = [r.randint(1,15) for x in range(rangeOfListsOne)]
listTwo = [r.randint(1,15) for x in range(rangeOfListsTwo)]

print(f"The list one is : {listOne} \nThe list two is: {listTwo}")

listOne.sort()
listTwo.sort()

print(f"The sorted list one is : {listOne} \nThe sorted list two is: {listTwo}")

def mergeSorted(listOne, listTwo): #! merge them into one list do no use sort method
    sortedList = list()
    i = 0
    j = 0
    while i < len(listOne) and j < len(listTwo): #! merging the list but here is always at least one remaining because one of them reaches the its limits
        if listOne[i] <= listTwo[j]:
            sortedList.append(listOne[i])
            i += 1
        elif listOne[i] > listTwo[j]:
            sortedList.append(listTwo[j])
            j += 1
# ! there is always one of the while functions is going to work because one ofd them is already rached its extreme value
    while i < len(listOne):#! adding remaining value of listOne
        sortedList.append(listOne[i])
        i += 1
    while j < len(listTwo):#! adding remaining value of listTwo
        sortedList.append(listTwo[j])
        j += 1
    return sortedList

print(f"The merged two list: {mergeSorted(listOne, listTwo)}")
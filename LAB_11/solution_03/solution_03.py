numberOne = "00000400029"
numberTwo = "00020301230"

def makeDictionary(number): #TODO: chancing the string numeric value to dictionary
    numberDictionary = {}
    for i, number in enumerate(number):
        if int(number) != 0:
            numberDictionary[i+1]= number
    return numberDictionary

def sparseArraySum(number1 , number2): #TODO: Vector sum of the two dictionarys to create a merged dictionary
    a = makeDictionary(number1)
    b = makeDictionary(number2)
    setOfTwoDictionarys = set(list(a.keys()) + list(b.keys()))
    print(setOfTwoDictionarys)
    merge = {key: int(a.get(key, 0)) + int(b.get(key, 0)) for key in setOfTwoDictionarys}
    return merge

def dictToArray(dictionary): #TODO: creating an array which filles wtih zeros, according to key of the merged dictionary change the zero with the value
    array = ["0" for x in numberOne]
    for key, value in dictionary.items():
        array[key - 1] = str(value)
    sparseArray = "".join(array)
    print(sparseArray)

def main():
    mergedDict = sparseArraySum(numberOne, numberTwo)
    dictToArray(mergedDict)
if __name__ == "__main__":
    main()
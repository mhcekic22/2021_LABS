FIRST_FILE = "solutionOne.txt"
SECONED_FILE = "solutionTwo.txt"
THIRD_FILE = "solutionThree.txt"


def functionOne(low, high): #TODO: first store all the numbers that are divisible by seven then remove all the number whose are divisible by 5
    firstList = []
    try:
        with open(FIRST_FILE, "w") as firstFile:
            for number in range(low, high + 1):
                if number % 7 == 0:
                    firstList.append(number)
            for number in firstList:
                if number % 5 == 0:
                    firstList.remove(number)
            for number in firstList:
                firstFile.write(str(number) + ",")
    except IOError as error:
        print(F"Something went wrong the error is : {error}")

def functionTwo(low, high): #TODO: Store all the numbers that are divisible by 7 but not 5 
    secondList = []
    try:
        with open(SECONED_FILE, "w") as secondFile:
            for number in range(low, high + 1):
                if number % 7 == 0 and number % 5 != 0:
                    secondList.append(number)
            for number in secondList:
                secondFile.write(str(number) + ",")
    except IOError as error:
        print(F"Something went wrong the error is : {error}")

def functionThree(low, high): #TODO: remove all the number which are divisible by 5 and for remaining store all the number which are divisible by 7
    thirdList = [x for x in range(low, high + 1)]
    finalList = []
    try:
        with open(THIRD_FILE, "w") as thirdFile:
            for number in thirdList:
                if number % 5 == 0:
                    thirdList.remove(number)
            for number in thirdList:
                if number % 7 == 0:
                    finalList.append(number)
            for number in finalList:
                thirdFile.write(str(number) + ",")
            
    except IOError as error:
        print(F"Something went wrong the error is : {error}")

def control():
    try:
        with open(FIRST_FILE) as firstFile, open(SECONED_FILE) as secondFile, open(THIRD_FILE) as thirdFile:
            lineOne = firstFile.readline()
            lineTwo = secondFile.readline()
            lineThree = thirdFile.readline()
            if lineOne == lineTwo == lineThree:
                return "They are all equal"
            else:
                return "They are not equal"
    except IOError as error:
        print(f"Something went wrog the error is : {error}")


def main():
    start = 2000
    finish = 3200
    functionOne(start, finish)
    functionTwo(start, finish)
    functionThree(start, finish)
    print(control())



if __name__ == "__main__":
    main()
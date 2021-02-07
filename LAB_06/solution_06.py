romanNumber = input("Enter the roman number: ")

def value(n, romanNumber):
    if romanNumber[n] == "M":
        return 1000
    elif romanNumber[n] == "D":
        return 500
    elif romanNumber[n] == "C":
        return 100
    elif romanNumber[n] == "L":
        return 50
    elif romanNumber[n] == "X":
        return 10
    elif romanNumber[n] == "V":
        return 5
    elif romanNumber[n] == "I":
        return 1
    else:
        return "you have been mistaken"


total = 0

for i in range(len(romanNumber)):
    if(len(romanNumber) == 1):
        total += value(0, romanNumber)
        break
    elif(value(0, romanNumber) >= value(1, romanNumber)):
        total += value(0, romanNumber)
        romanNumber = romanNumber[1:]
    else:
        total += value(1, romanNumber) - value(0, romanNumber)
        romanNumber = romanNumber[2:]
        
print("The result is : ",  total)
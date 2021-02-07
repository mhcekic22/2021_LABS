number = ["1", "4", "9", "16", "9", "7", "4", "9", "11"]

numberRange = len(number)

def reverse(number, numberRange):
    numberReverse = list()
    
    for i in range(numberRange):
        numberReverse.append(number[-(i+1)])
    
    return numberReverse

print(reverse(number, numberRange))
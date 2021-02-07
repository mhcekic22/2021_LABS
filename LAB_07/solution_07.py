def sumWithoutSmallest(numbers):
    minimum = min(numbers)
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    
    return total - (2 * minimum)

number = [1, 4, 9, 16, 9, 7, 4, 9, 11]

print(sumWithoutSmallest(number))
number = int(input("Enter 5-digit numbers: "))

digits = [int(x) for x in str(number)]

for i in range(len(digits)):
    print(digits[i], end=" ")
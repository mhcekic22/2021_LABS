number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if (number1 > number2) and (number2 > number3):
    print("The sequence is decreasing")
elif (number1 < number2) and (number2 < number3):
    print("The sequence is increasing")
else:
    print("You should enter properly")
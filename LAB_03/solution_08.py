firstUnit = input("Enter the firs unit: ")
value1 = float(input("Enter the value: "))

if firstUnit == "mm" or firstUnit == "cm" or firstUnit == "m" or firstUnit == "km":
    secondUnit = input("Enter the second unit: ")
    if (firstUnit == "mm" and secondUnit == "inch"):
        value2 = value1 * 0.0393701
    elif (firstUnit == "cm" and secondUnit == "inch"):
        value2 = value1 * 0.393701
    elif (firstUnit == "m" and secondUnit == "inch"):
        value2 = value1 * 39.3701
    elif (firstUnit == "km" and secondUnit == "inch"):
        value2 = value1 * 39370.1
    else:
        print("You have been mistaken")
elif firstUnit == "g" or firstUnit == "kg":
    secondUnit = input("Enter the second unit: ")
    if (firstUnit == "g" and secondUnit == "lb"):
        value2 = value1 * 0.00220462
    elif (firstUnit == "kg" and secondUnit == "lb"):
        value2 = value1 * 2.
    else:
        print("You have been mistaken")
elif firstUnit == "ml" or firstUnit == "l":
    secondUnit = input("Enter the second unit: ")
    if (firstUnit == "ml" and secondUnit == "gal"):
        value2 = value1 * 0.000264172
    elif (firstUnit == "l" and secondUnit == "gal"):
        value2 = value1 * 0.264172
    elif (firstUnit == "ml" and secondUnit == "oz"):
        value2 = value1 * 0.033814
    elif (firstUnit == "l" and secondUnit == "oz"):
        value2 = value1 * 33.814
    else:
        print("You have been mistaken")
else:
    print("You have been mistaken")
    
print("%.1f %s is %s: %.1f" % (value1, firstUnit, secondUnit, value2))
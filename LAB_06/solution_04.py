def calculation(income, numberOfChildren):
    errorMessage = "You are not allowed"
    if income < 20000:
        benefit = 2000
    elif 20000 <= income < 30000 and numberOfChildren >= 2:
        benefit = 1500
    elif 30000 <= income < 40000 and numberOfChildren >= 3:
        benefit = 1000
    else:
        return errorMessage
    return benefit * numberOfChildren
    

income = 0

while True:
    income = int(input("Enter the annual income: "))
    if income == -1:
        break
    numberOfChildren = int(input("Enter the number of children: "))
    print("The financial aid is: ", calculation(income, numberOfChildren))
    

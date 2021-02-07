initialBallance = float(input("Enter the initial ballance: "))
yearOfDeposit = int(input("Enter the year of deposit: "))

def interestCalculation(initialBallance, yearOfDeposit):
    yearInterest = 0.12
    for _ in range(yearOfDeposit):
        profit = initialBallance * yearInterest
        initialBallance += profit
        
    return initialBallance

print("Interest calculation with initial ballance of %.1f and for %d year is: %.1f" % (initialBallance, yearOfDeposit, (interestCalculation(initialBallance, yearOfDeposit))))
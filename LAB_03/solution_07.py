status = input("married or unmerried: ")

income = int(input("income: "))

if status == "unmerried":
    if (0 < income < 8000):
        tax = income * 0.1
    elif (8000 < income < 32000):
        tax = 800 + income * 0.15
    else:
        tax = 4400 + income * 0.25
elif status == "married":
    if (0 < income < 16000):
        tax = income * 0.1
    elif (16000 < income < 6400):
        tax = 1600 + income * 0.15
    else:
        tax = 8800 + income * 0.25

print("The fax is %i" % tax)

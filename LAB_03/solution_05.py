while True:
    try:
        year = input("Enter the year: ")
        if (len(year) ==  4) and (year.isdigit()):
            break
        else:
            print("You should enter 4-digit number")
    except ValueError:
        print("You should enter a integer")
        continue

if int(year) % 4 == 0:
    flag = 1
    if int(year) % 100 == 0:
        flag = 0
    if int(year) % 400 == 0:
        flag = 1
else:
    flag = 0

if flag:
    print("It is a leap year")
else:
    print("It is not a leap year")
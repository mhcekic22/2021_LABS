def months(i):
    switcher1 = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    return switcher1.get(i, "default")

def days(i):
    switcher2 = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    return switcher2.get(i, "default")

month = input("Enter the month name: ")

day = int(input("Enter the day number: "))

monthNumber = months(month)

if monthNumber == 1 or monthNumber == 2 or monthNumber == 3:
    season = "Winter"
elif monthNumber == 4 or monthNumber == 5 or monthNumber == 6:
    season = "Spring"
elif monthNumber == 7 or monthNumber == 8 or monthNumber == 9:
    season = "Summer"
elif monthNumber == 10 or monthNumber == 11 or monthNumber == 12:
    season = "Fall"

if (monthNumber % 3 == 0) and (day >= 21):
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"
        
print("The season is: ", season)






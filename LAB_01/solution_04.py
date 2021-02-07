def months(i):
    switcher ={
        "January": 1,
                
        "February": 2,
                
        "March": 3,
                
        "April": 4,
                
        "May": 5,
                
        "June": 6,
                
        "July": 7,
                
        "August": 8,
                
        "September": 9,
                
        "October": 10,
                
        "November": 11,
                
        "December": 12
    }
    return switcher.get(i, "default")

month = input("Enter the month name: ")

ay = int(months(month))

print("the valuse is", ay)

if (ay < 4):
    print("The season is Winter")
elif (3 < ay < 7):
    print("The season is Spring")
elif (6 < ay < 10):
    print("The season is Summer")
else:
    print("The season is Fall")
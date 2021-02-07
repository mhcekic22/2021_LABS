def grades(i):
    switcher = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0
    }
    return switcher.get(i, "default")

note = input("Enter the note (A, B, C, D, F): ")

number = grades(note[0])

if (note[1] == "+"):
    number += 0.3
elif (note[1] == "-"):
    number -= 0.3
else:
    print("You should enter proparly")

if number > 4:
    number = 4
elif note[0] == "F":
    number = 0
print("Your note is: ", number)
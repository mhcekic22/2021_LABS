grade = float(input("Enter the number: "))

gradeRounded = round(grade, 1)

if(gradeRounded > 3.5):
    if abs(gradeRounded - 4) == 0 :
        print("The grade is A+")
    elif abs(gradeRounded - 4) < abs(gradeRounded - 3.7):
        print("The grade is A")
    else:
        print("The grede is A-")

if (3.5 > gradeRounded > 2.5):
    if abs(gradeRounded - 3.3) < abs(gradeRounded - 3):
        print("The grade is B+")
    elif abs(gradeRounded - 3) < abs(gradeRounded - 2.7):
        print("The grade is B")
    else:
        print("The grede is B-")

if (2.5 > gradeRounded > 1.5):
    if abs(gradeRounded - 2.3) < abs(gradeRounded - 2):
        print("The grade is C+")
    elif abs(gradeRounded - 2) < abs(gradeRounded - 1.7):
        print("The grade is C")
    else:
        print("The grede is C-")

if (1.5 > gradeRounded): 
    if abs(gradeRounded - 1.3) < abs(gradeRounded - 1):
        print("The grade is F+")
    elif abs(gradeRounded - 1) < abs(gradeRounded - 0.7):
        print("The grade is F")
    else:
        print("The grede is F-")
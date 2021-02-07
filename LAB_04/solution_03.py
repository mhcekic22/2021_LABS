number = int(input("Enter the number:"))

for i in range(number):
    for j in range(number):
        print("*", end="")
    print("\n")
    
for i in range(number):
    print(" "*(number - i), "*"*i, "*", "*"*i, " "*(number - i), "\n", end="", sep="")
    if i == number-1:
        for j in range(2, number+1):
            print(" "*j, "*"*(number - j), "*", "*"*(number - j), " "*j, "\n", end="", sep="")
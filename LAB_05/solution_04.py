rOld = int(input("Enter the r old: "))

a = 32310901
b = 1729 
m = 2**24

for i in range(100):
    rNew = (a * rOld + b) % m
    print("The %d. integer is %d" % (i+1, rNew))
    rOld = rNew
number = int(input("Enter the number: "))

for i in range(2, number):
    counter = 0
    for j in range(1, i):
        if i % j == 0:
            counter += 1
    if counter == 1:
        print("%d" % i)
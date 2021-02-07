number = int(input("Enter the number: "))

counter = 2
while number != 1:
    if number % counter == 0:
        print(counter)
        number /= counter
    else:
        counter += 1

print("It is finished.")
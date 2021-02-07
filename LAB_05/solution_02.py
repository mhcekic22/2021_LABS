pin = "1234"

counter = 0

while counter != 3:
    guess = input("Enter the password: ")
    if guess == pin:
        print("Your pin is correct")
        break
    else:
        print("Your pin is incorrect")
        counter += 1

if counter == 3:
    print("Your card is blocked")

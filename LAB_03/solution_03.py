sentence = input("Enter the sentence: ")

if sentence.isalpha():
    print("It contains only letters")
    if sentence.isupper():
        print("It contains only uppercase letters")
    if sentence.islower():
        print("It contains only lowercase letters")
if sentence.isnumeric():
    print("It contains only digits")
if sentence.isalnum():
    print("It contains only letters and numbers")
if sentence[0].isupper():
    print("The first letter is a capital letter")
if sentence[-1] == ".":
    print("It ends with a period")
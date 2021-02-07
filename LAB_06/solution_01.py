vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "o", "U")

sentence = input("Enter the string: ")

def countVowels(string):
    counter = 0
    for i in range(len(string)):
        if string[i] in vowels:
            counter += 1
    return counter

print("the number of the vowels in the sentence is:", countVowels(sentence))
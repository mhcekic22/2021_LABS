sentence1 = list(input("Enter the sentence: "))

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

upperCase = list()
sentence2 = list()
counterIndexList = list()

length = len(sentence1)

counter = 0
counterIndex = 0

for i in range(length):
    counterIndex += 1
    sentence2.append(sentence1[i])
    if sentence1[i].isupper():
        upperCase.append(sentence1[i])
    if sentence1[i] in vowels:
        counterIndexList.append(counterIndex)
        sentence2[i] = "_"
    if sentence1[i].isdigit():
        counter += 1
        
print("The only uppercase letters are: ", upperCase)

print("The second letter of the string: ", sentence1[1])

print("The vowels are replaced with underscore: ", sentence2)

print("The number of digits in string is: ", counter)

print("The position of all vowels in the string: ", counterIndexList)
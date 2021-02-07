word = input("Enter the word: ")

for i in range(len(word)):
    for j in range(len(word)-i):
        print(word[j:j+i+1])
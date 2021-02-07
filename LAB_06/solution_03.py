sentence = input("Enter the sentence: ")
word = input("Enter the word: ")

def find(string, hint):
    if hint in sentence:
        flag = True
    else:
        flag = False
    return flag

b = find(sentence, word)

print("The b is: ", b)
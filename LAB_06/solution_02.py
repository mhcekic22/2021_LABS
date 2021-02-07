sentence = input("Enter the sentence: ")

def countWords(string):
    wordCounter = 1
    sperator = " "
    for i in range(len(string)):
        if string[i] == sperator:
            wordCounter += 1
        
    return wordCounter

print("There are %d words in the sentence." % countWords(sentence))
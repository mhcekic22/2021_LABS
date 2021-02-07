BAD_WORDS_FILE = "badWords.txt"
TEXT_FILE = "text.txt"
TEXT_WITH_CENSOR_FILE = "textWithCensor.txt"

def main():
    
    try:
        with open(BAD_WORDS_FILE, "r") as badFile:
            
            badWords = set()
            for line in badFile:
                line = line.rstrip()
                words = line.split(" ")
                for word in words:
                    badWords.add(word)
                    
        with open(TEXT_FILE, "r") as textFile:
            
            textWords = []
            
            for line in textFile:
                line = line.rstrip()
                words = line.split(" ")
                for word in words:
                    textWords.append(word)
                textWords.append("\n")
            
            for position, word in enumerate(textWords):
                if word in badWords:
                    textWords[position] = "*"*len(word)
            
        with open(TEXT_WITH_CENSOR_FILE, "w") as censorFile:
            
            for word in textWords:
                if word == "\n":
                    censorFile.write(word)
                else:
                    censorFile.write(word + " ")
                
    except IOError as error:
        print(f"An error has occured and the error is: {error}")


if __name__ == "__main__":
    main()
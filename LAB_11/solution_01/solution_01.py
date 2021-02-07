FILE_NAME = "text.txt"

def main():
    
    wordDictionary = dict()
    
    try:
        with open(FILE_NAME) as f:
            for line in f:
                line = line.strip()
                words = line.split(" ")
                for word in words:
                    if word in wordDictionary:
                        wordDictionary[word] = wordDictionary[word] + 1
                    else:
                        wordDictionary[word] = 1
                        
        tupleSortedWordDictionary = sorted(wordDictionary.items(), key = lambda x: x[1], reverse = True)
        
        sortedWordDictionary = {key: val for key, val in tupleSortedWordDictionary}
        
        first100CommonWords = dict(list(sortedWordDictionary.items())[:100])
        
        print(len(first100CommonWords))
        
        for key in first100CommonWords:
            print(f" {key}: {first100CommonWords[key]}")

    except IOError as error:
        print(f"An error has occured in {FILE_NAME} the error is {error}")

if __name__ == '__main__':
    main()
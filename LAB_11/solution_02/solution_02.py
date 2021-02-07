alphabet = "abcdefghijklmnopqrstuvwxyz"
def main():
    firstString = input("Enter the first string: ")
    secondString = input("Enter the second string: ")
    #firstStringL = [char for char in firstString]
    #secondStringL = [char for char in secondString]
    #commonCharacters = [char for index, char in enumerate(firstStringL) if char in secondStringL and char not in firstStringL[0:index]] #! i used list to find comkon strings
    firstStringS = {char for char in firstString}
    secondStringS = {char for char in secondString}
    commonCharactersS = {char for char in firstStringS if char in secondStringS}
    uniqueCharOfFirstString = {char for char in firstString if char not in secondStringS}
    bothStrings = {char for char in firstString + secondString}
    charDontOccur = {char for char in alphabet if char not in bothStrings}
    print(f"The first string is >>{firstString}<< and the second string is >>{secondString}<<")
    print(f"The common characters of two strings are {commonCharactersS}")
    print(f"The unique characters of first string that are not in the second string {uniqueCharOfFirstString}")
    print(f"The chars do not occurs in bot strings are {charDontOccur}")
if __name__ == '__main__':
    main()
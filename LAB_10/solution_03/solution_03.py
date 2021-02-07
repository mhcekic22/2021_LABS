fileList = []
fileName = " "

while fileName != "0":
    fileName = input("Enter the file names that you want to search the words: ")
    fileList.append(fileName)

if fileList[-1] == "0":
    fileList.pop()
    print(fileList)
else:
    print(fileList)

wordForSearch = input("Enter the word that you want to serch: ")
wordForSearchLower = wordForSearch.lower()

for i in range(len(fileList)):
    file = open(fileList[i], 'r')
    lines = file.readlines()
    for j in range(len(lines)):
        lowerLines = lines[j].lower()
        if wordForSearchLower in lowerLines:
            print(f"{fileList[i]}: {lines[j]}")
    file.close()

print("The search has ended")
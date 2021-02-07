countryName = input("Enter the country name: ")
exceptions = ("Beliz", "Belizele", "Cambodge", "Mexiquele", "Mozambiquele", "Zaïre", "Zimbabwe")
vowels = ("A", "E", "I", "O", "U")
space = (" ")
counter = 0

countryNameArray = list()

for i in range(len(countryName)):
    countryNameArray.append(countryName[i])
    if countryNameArray[i] in space:
        countryNameArray[i] = "-"
        counter = i
    
if countryNameArray[-1] == "e" and countryName not in exceptions:
    countryNameArray.insert(0, "la")
    countryNameArray.insert(1, " ")
elif (countryNameArray[0] in vowels) and not countryNameArray[counter] == "-":
    countryNameArray.insert(0, "l'")
elif countryNameArray[counter] == "-":
    countryNameArray.insert(0, "les")
    countryNameArray.insert(1, " ")
else:
    countryNameArray.insert(0, "le")
    countryNameArray.insert(1, " ")

countryName = "".join(countryNameArray)

print(countryName)
inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

lines = inFile.readlines()

i = len(lines) - 1

while i >= 0:
    outFile.write(lines[i])
    i -= 1

inFile.close()
outFile.close()

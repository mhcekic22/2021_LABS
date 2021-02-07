inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

lines = inFile.readlines()

for i in range(len(lines)):
    line = f"/*{i + 1}*/ {lines[i]}"
    outFile.write(line)

inFile.close()
outFile.close()
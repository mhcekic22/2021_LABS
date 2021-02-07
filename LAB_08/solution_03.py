N = int(input("Enter the range: "))
table = [[0 for i in range(N)] for j in range(N)]
controlTable = []

def printingTable(table):            
    for i in range(N): # printing the table
        for j in range(N):
            print(table[i][j], end="   ")
        print("\n")
i = 0
j = 0
while i < N: # Enntering the data in some restrictions
    while j < N:
        number = int(input(f"Enter the [{i + 1}][{j + 1}] number: "))
        if (number in range(1, N**2 + 1)) and (number not in controlTable):
            table[i][j] = number
            controlTable.append(number)
            j += 1
            printingTable(table)
        else:
            print(f"{number} is used before or out of range, try another number")
    i += 1
    j = 0
    
def rowCheck(table): # checking the rows
    resultOne = 0
    resultTwo = 0
    i = 0
    while i < (len(table) - 1):
        resultOne = sum(table[i])
        resultTwo = sum(table[i+1])
        if resultOne != resultTwo:
            i = len(table) - 1
            return False
        else:
            i += 1
    return True

def columnCheck(table): # checking the columns
    resultOne = 0
    resultTwo = 0
    i = 0
    j = 0
    while j < len(table) - 1:
        while i < len(table):
            resultOne += table[i][j]
            resultTwo += table[i][j+1]
            i += 1
        if resultOne != resultTwo:
            return False
        else:
            j += 1
    return True

def diagonalCheck(table): # checking the diagonals
    resultOne = 0
    resultTwo = 0
    i = 0
    j = len(table) - 1
    while i < len(table):
        resultOne += table[i][i]
        i += 1
    while j >= 0:
        resultTwo += table[j][j]
        j -= 1
    if resultOne != resultTwo:
        return False
    else:
        return True

def magicSquare(table):
    if rowCheck(table) and columnCheck(table) and diagonalCheck(table):
        return "It is a magic square"
    else:
        return "It is not a magic square"
    
print(magicSquare(table))
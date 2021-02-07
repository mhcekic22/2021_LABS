table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def tableMaker(table):
    rowBorder = "+---+---+---+"
    print("",rowBorder)
    for i in range(3):
        for j in range(3):
            print(f" | {table[i][j]}", end="")
        print(" | ", end="")
        print("\n", rowBorder)

def tableChecker(table, boardRow, boardColumn): #TODO: check if the chosen place is empty or not
    if table[boardRow][boardColumn] != " ":
        return False
    else:
        return True

def tablePlacerFirst(table, boardRow, boardColumn): #TODO: place the choosen value for first player
    table[boardRow][boardColumn] = "X"
    return table

def tablePlacerSecond(table, boardRow, boardColumn): #TODO: place the choosen value for second player
    table[boardRow][boardColumn] = "O"
    return table

def tableRowChecker(table): #TODO check the rows of the board
    i = 0
    j = 0
    while i < len(table):
        counterX = 0
        counterO = 0
        j = 0
        while j < len(table):
            if table[i][j] == "X":
                counterX += 1
                j += 1
            elif table[i][j] == "O":
                counterO += 1
                j += 1
            else:
                j += 1
        if counterX == 3:
            return 1
        elif counterO == 3:
            return 2
        else:
            i += 1
                

def tableColumnChecker(table): #TODO check the columns of the board
    i = 0
    j = 0
    while j < len(table):
        counterX = 0
        counterO = 0
        i = 0
        while i < len(table):
            if table[i][j] == "X":
                counterX += 1
                i += 1
            elif table[i][j] == "O":
                counterO += 1
                i += 1
            else:
                i += 1
        if counterX == 3:
            return 1
        elif counterO == 3:
            return 2
        else:
            j += 1

def tableDiagonalChecker(table): #TODO check the diagonals of the board
    i = 0
    counterX = 0
    counterO = 0
    while i < len(table):
        if table[i][i] == "X":
            counterX += 1
            i += 1
        elif table[i][i] == "O":
            counterO += 1
            i += 1
        else:
            i += 1
    if counterX == 3:
        return 1
    elif counterO == 3:
        return 2
    else:
        counterX = 0
        counterO = 0
    j = 0
    while j < 3:
        if table[len(table) - 1 - j][j] == "X":
            counterX += 1
            j += 1
        elif table[len(table) - 1 - j][j] == "O":
            counterO += 1
            j += 1
        else:
            j += 1
    if counterX == 3:
        return 1
    elif counterO == 3:
        return 2

def winnerChecker(table): #TODO check the winner
    if tableRowChecker(table) == 1 or tableColumnChecker(table) == 1 or tableDiagonalChecker(table) == 1:
        return 1
    elif tableRowChecker(table) == 2 or tableColumnChecker(table) == 2 or tableDiagonalChecker(table) == 2:
        return 2
    else:
        return 3

tableMaker(table)
counter = 0 
flag = 0
while counter < 9 and flag == 0:
    if counter % 2 == 0: 
        print("Player 1's turn")
        boardRow = int(input("Enter the row number: "))
        boardColumn = int(input("Enter the column number: "))
        if boardRow in range(0,3) and boardColumn in range(0,3) and tableChecker(table, boardRow, boardColumn):
            counter += 1
            tablePlacerFirst(table, boardRow, boardColumn)
        else:
            print("Choose a proper row and column")
    else:
        print("Player 2's turn")
        boardRow = int(input("Enter the row number: "))
        boardColumn = int(input("Enter the column number: "))
        if boardRow in range(0,3) and boardColumn in range(0,3) and tableChecker(table, boardRow, boardColumn):
            counter += 1
            tablePlacerSecond(table, boardRow, boardColumn)
        else:
            print("Choose a proper row and column")
    tableMaker(table)
    if winnerChecker(table) == 1:
        print("Player One won")
        flag = 1
    elif winnerChecker(table) == 2:
        print("Playe Two won")
        flag = 1
    else:
        flag = 0

if counter == 9 and flag != 1:
    print("The board is drawn")


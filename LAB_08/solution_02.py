import random as r

rangeTable = int(input("Enter the range: "))

values = [[r.randint(0, 9) for row in range(rangeTable)] for column in range(rangeTable)]

for i in range(len(values)):
    for j in range(len(values[0])):
        print(values[i][j], end="   ")
    print("\n")

row = int(input("Input the row number: "))
column = int(input("Input the column number: "))

def neighborAverage(values, row, column):
    result = 0
    rowStart = 0
    columnStart = 0
    rowEnd = 0
    columnEnd = 0
    divisor = 0
    if row == 0:
        rowStart = row
        rowEnd = row + 2
        if column == 0: # row = 0 and column = 0 
            columnStart = column
            columnEnd = column + 2
            divisor = 3
        elif column == len(values[1]) - 1: # row = 0 and column = max
            columnStart = column - 1
            columnEnd = column + 1
            divisor = 3
        else: # row = 0 and column is in between
            columnStart = column - 1
            columnEnd = column + 2
            divisor = 5
    elif row == len(values) - 1:
        rowStart = row - 1
        rowEnd = row + 1
        if column == 0: # row = max and column = 0
            columnStart = column
            columnEnd = column + 2
            divisor = 3
        elif column == len(values[1]) - 1: # row = max and column = max
            columnStart = column - 1
            columnEnd = column + 1
            divisor = 3
        else: #row = max column is in between
            columnStart = column - 1
            columnEnd = column + 2
            divisor = 5
    elif (column == 0) and (row != 0) and (row != len(values) - 1): # column = 0 row is in between
            rowStart = row - 1
            rowEnd = row + 2
            columnStart = column
            columnEnd = column + 2
            divisor = 5
    elif (column == len(values) - 1) and (row != 0) and (row != len(values) - 1): #column = max row is in between
            rowStart = row - 1
            rowEnd = row + 2
            columnStart = column - 1
            columnEnd = column + 1
            divisor = 5
    else: # all the values when row and clumn are not in extremes
            rowStart = row - 1
            rowEnd = row + 2
            columnStart = column - 1
            columnEnd = column + 2
            divisor = 8
            
    for i in range(rowStart, rowEnd):
        for j in range(columnStart, columnEnd):
            result += values[i][j]
    result = (result - values[row][column]) / divisor
    return result

print("The result is: " , neighborAverage(values, row, column))

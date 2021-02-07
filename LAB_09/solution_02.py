seats =    [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],  # ! 10 by 9
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], 
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], 
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
            [20, 20, 30, 30, 40, 40, 30, 30, 20, 20], 
            [20, 30, 30, 40, 50, 50, 40, 30, 30, 20], 
            [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]

def printSeats(seats): # printing the seats
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            print(seats[i][j], end="   ")
        print("\n")

def checkSeatsBySeat(seats, seatRow, seatColumn):
    flag = 0
    if seats[seatRow][seatColumn] != 0:
        seats[seatRow][seatColumn] = 0
        flag = 1
    elif seats[seatRow][seatColumn] == 0:
        flag = 0
    if flag == 1:
        return True
    else:
        return False

def checkSeatsByPrice(seats, price):
    i = 0
    j = 0
    while i < len(seats):
        j = 0
        while j < len(seats[0]):
            if seats[i][j] == price:
                seats[i][j] = 0
                i = len(seats)
                break
            else:
                j += 1
        i += 1
    return seats

numberOfSeats = len(seats) * len(seats[0])

prices = [10, 20, 30, 40, 50]

while numberOfSeats > 0: #TODO:numberOfSeats will be done later
    printSeats(seats)
    choice = input("Enter price or seat number: ")
    if choice == "price": #TODO: change first chosen seat which equals to price to zero
        price = int(input("Enter the price: "))
        if price in prices:
            checkSeatsByPrice(seats, price)
            numberOfSeats -= 1  
            print(f"Remaining number of seat is: {numberOfSeats}")
        else:
            print("price not in prices you must choose a proper one")
    elif choice == "seat": #TODO: check if it is free, if it is free change it to zero
        seatRow = int(input("Enter the row of seats: "))
        seatColumn = int(input("Enter the column of seats: "))
        if seatRow in range(len(seats)) and seatColumn in range(len(seats[0])):
            if checkSeatsBySeat(seats, seatRow, seatColumn):
                print("Seat is available")
                numberOfSeats -= 1
            else:
                print("Seat is NOT available choose another one")
            print(f"Remaining number of seat is: {numberOfSeats}")
        else:
            print("You must choose a proper seat")
    else:
        print("you must choose price or seat")

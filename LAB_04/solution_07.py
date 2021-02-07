from random import randint

pileSize = randint(10, 100)
start = randint(0, 1)
print("The starter pile size is: %d" % pileSize)
while pileSize != 0:
    if start == 1:
        if pileSize == 1:
            print("You lost")
            break
        choicePerson = int(input("It is your turn, enter the number: "))
        if 1<=choicePerson<=pileSize//2:
            pileSize -= choicePerson
            print("You choosed %d and the pile size is: %d" % (choicePerson, pileSize))
            start = 0
        else:
            print("You should choose properly")
            start = 1
    elif start == 0:
        if pileSize == 1:
            print("You win")
            break
        brain = randint(0, 1)
        if brain:
            if pileSize > 63:
                smartChoice = pileSize - 63
            elif 63 > pileSize > 31:
                smartChoice = pileSize - 31
            elif 31 > pileSize > 15:
                smartChoice = pileSize - 15
            elif 15 > pileSize > 7:
                smartChoice = pileSize - 7
            elif 7 > pileSize > 3:
                smartChoice = pileSize - 3
            else:
                smartChoice = randint(1, pileSize//2)
            
            pileSize -= smartChoice
            print("The computer choosed %d and the pile size is: %d" % (smartChoice, pileSize))
            start = 1
        else:
            stupidChoice = randint(1, pileSize//2)
            pileSize -= stupidChoice
            print("The computer choosed %d and the pile size is: %d" % (stupidChoice, pileSize))
            start = 1
            
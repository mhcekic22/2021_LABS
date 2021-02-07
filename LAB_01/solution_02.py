friends = int(input("How many friends:"))

cost = float(input("The cost of the night:"))

rate = 15/100

tip = cost * rate

totalCost = cost + tip

totalPeople = friends + 1

totalCostForEach = totalCost / totalPeople

totalTipForEach = tip / totalPeople

print("The total cost of the night is :", totalCost)
print("The total cost for each person:", totalCostForEach)
print("The total tip for each person:", totalTipForEach)

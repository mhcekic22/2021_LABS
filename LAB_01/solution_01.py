distance = float(input("Enter the distance between home and the school:"))

while True:
    try:
        value = input("type m for mile, km for kilometer:")
        if value == "m" or value == "km":
            print ("Type of the distance is:", value)
            break
        else:
            print ("You should enter m or km")
    except ValueError:
        print ("You should enter a keyword")
        continue

days = int(input("How many days you go to work:"))

mile = 1.60934

if value == "m":
    distance = distance * mile
else:
    print("You have to enter m or km")
    
print ("The distance is in km :" , distance)
    
distance = 2 * days * distance
    
print ("You go" , days , "days to work and its takes" , distance , "km")


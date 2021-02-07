money = 1000
rate = 0.05

year = int(input("Enter the year of interest:"))

for i in range(year):
    money = (money * rate) + money

print("After", year, "The total amaount of money is:", money)
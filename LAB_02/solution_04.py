totalPriceOfBooks = int(input("Enter the total price of the books: "))
numberOfBooks = int(input("Enter the number of books: "))

tax = totalPriceOfBooks * 0.075

shippingCharge = numberOfBooks * 2

price = totalPriceOfBooks + tax + shippingCharge

print("The total price of is: ", price)
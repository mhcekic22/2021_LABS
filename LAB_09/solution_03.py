def nameOfBestCustomer(customers, sales):
    maxSale = max(sales)
    for i in range(len(sales)):
        if sales[i] == maxSale:
            return customers[i]

customers = list()
sales = list()

price = 1

while price != 0: # Entering the name and the sales
    nameCustomer = input("Enter the name of customer: ")
    customers.append(nameCustomer)

    saleCustomer = int(input("Enter the sale: "))
    sales.append(saleCustomer)
    
    price = saleCustomer
    

print("The name of the best customer is: ", nameOfBestCustomer(customers, sales))

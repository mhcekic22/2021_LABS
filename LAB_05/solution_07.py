totalTicketNumber = 100
maxTicketNumber = 4
people = 0

while totalTicketNumber > 0:
    ticketNumber = int(input("Enter the numbers of ticket that you want to: "))
    if totalTicketNumber <= maxTicketNumber:
        maxTicketNumber = totalTicketNumber
    if ticketNumber <= maxTicketNumber:
        totalTicketNumber -= ticketNumber
        print("The remaining ticket is %d:" % totalTicketNumber)
        people += 1
    else:
        print("You cant buy more than %d tickets" % maxTicketNumber)

print("%d people bought the tickets." % people)
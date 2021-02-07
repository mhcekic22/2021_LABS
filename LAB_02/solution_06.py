phone = input("Enter the phone number: ")

firstThree = phone[:3]

secondThree = phone[3:6]

rest = phone[6:]

print("(%s)%s-%s" % (firstThree, secondThree, rest))
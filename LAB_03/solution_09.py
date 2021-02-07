money = float(input("Enter how much you spend: "))

if money < 10:
    coupon = 0
elif 10 <= money < 60:
    coupon = money * 0.08
elif 60 <= money < 150:
    coupon = money * 0.10
elif 150 <= money < 210:
    coupon = money * 0.12
elif 210 <= money:
    coupon = money * 0.14
else:
    print("You have been mistaken")

print("Your coupon is : %.2f" % coupon)
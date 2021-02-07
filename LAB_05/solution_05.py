A = 0.1
B = C = 0.01
D = 0.00002 
predN = 20
preyN = 1000

period = int(input("Enter the preiod number: "))

for i in range(period):
    preyNn = preyN * (1 + A - B + predN)
    predNn = predN * (1 - C + D * preyN)
    preyN = preyNn
    predN = predNn

print("The preyN is: %.1f" % preyN)
print("The predN is: %.1f" % predN)
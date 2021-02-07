a = ("1", "2", "3", "4", "5","5","4", "5","5", "5","5", "5","5", "5","5", "5","5", "5","5","4", "5","5","4")
b = ("1", "2", "3", "4", "5","5","4", "2", "3", "4", "5","5","4", "2", "3", "4", "5","5","4", "5")

lengthA = len(a)
lengthB = len(b)

def sameSet(a, b, lengthA, lengthB):
    aOnly = list()
    bOnly = list()
    
    for i in range(lengthA):
        for j in range(lengthA):
            if a[i] == a[j] not in aOnly:
                aOnly.append(a[j])

    for i in range(lengthB):
        for j in range(lengthB):
            if b[i] == b[j] not in bOnly:
                bOnly.append(b[j])

    if aOnly == bOnly:
        return "They are equal"
    else:
        return "They are not equal"

print(sameSet(a, b, lengthA, lengthB))
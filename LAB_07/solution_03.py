a = ("1", "2", "3", "4", "5")
b = ("1", "2", "3", "d", "5")

n = len(a)

def equal(a, b, n):
    flag = True
    for i in range(n): 
        if a[i] != b[i]: 
            flag = False
    if flag:
        return "They are equal"
    else:
        return "They are not equal"
        
print(equal(a, b, n))
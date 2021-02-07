names = list()

for i in range(3):
    name = input("Enter the name:")
    names.append(name)

for i in range(len(names)):
    for j in range(i+1, len(names)):
        if names[i] > names[j]:
            holder = names[i]
            names[i] = names[j]
            names[j] = holder
            
print(names)
values = [4.0, 6.0, 6.5, 2.3, 4.3, 6.0, 43.0, 6.0, 7.0, 6.0, 6.0, 6.4, 76]

average = sum(values) / len(values)

counter = 0
counter2 = 0

while True:
    average = sum(values) / len(values)
    print("average is: ", round(average, 3))
    if counter == 0:
        print("abov")
        values[counter] = (values[counter] + values[counter+1])/2
        values[counter] = round(values[counter], 3)
        counter += 1
    elif counter == len(values)-1:
        values[counter] = (values[counter] + values[counter-1])/2
        values[counter] = round(values[counter], 3)
        counter = 0
    else:
        values[counter] = (values[counter] + values[counter+1] + values[counter-1])/3
        values[counter] = round(values[counter], 3)
        counter += 1
    if round(average, 1) == round(values[counter], 1):
        if round(average, 1) == round(values[-counter], 1):
            break
    counter2 +=1

print(values)
print(counter2)
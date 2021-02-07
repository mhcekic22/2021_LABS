def main():
    rangeOfNumbers = int(input("Enter the range of the number set: ")) # ! for setting the range
    lastNumber = rangeOfNumbers + 1
    numbers = {x for x in range(1, lastNumber)} # ! setting the set of numbers according to the range

    print(numbers)
    if 1 in numbers:
        numbers.discard(1)

    i = 2
    while i < lastNumber:
        for j in range(i, lastNumber):
            if i != j and j % i == 0:
                numbers.discard(j)
        print(numbers)
        i += 1
    print(numbers)




if __name__ == "__main__":
    main()
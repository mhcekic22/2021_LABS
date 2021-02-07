start1 = 10
end1 = 12

start2 = 11
end2 = 13

if start1 > start2:
    start = start1
else:
    start = start2

if end1 < end2:
    end = end1
else:
    end = end2

if start > end:
    print("The appointments are overlapping")
else:
    print("The appointmens don't overlap")
listFirst = [1, 4, 9, 16]
listSecond = [9, 7, 4, 9, 11]
listMerge = list()

def merge(listFirst, listSecond, merge):
    if len(listFirst) <= len(listSecond):
        for i in range(len(listSecond)):
            if i < len(listFirst) :
                merge.append(listFirst[i])
                merge.append(listSecond[i])
            else:
                merge.append(listSecond[i])
    else:
        for i in range(len(listFirst)):
            if i < len(listSecond):
                merge.append(listSecond[i])
                merge.append(listFirst[i])
            else:
                merge.append(listFirst[i])
    return listMerge

print(merge(listFirst, listSecond, listMerge))
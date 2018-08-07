def findIfAdjacentNumberAreEqual(list):
    previous=-1
    flag = False
    for value in list:
        if previous == value:
            flag = True
        previous = value
    return flag

print(findIfAdjacentNumberAreEqual([1,2,3]))
print(findIfAdjacentNumberAreEqual([1,2,3,3]))
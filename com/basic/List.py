def listOfnumebrs(operation,list,number=0):
    if operation=="append":
        list.append(number)
        print(list)
    if operation=="reverse":
        list.reverse()
        print(list)
    if operation=="sort":
        list.sort()
        print(list)


listOfnumebrs("append",[1,2,3,4],9)
listOfnumebrs("sort",[1,6,3,2])
listOfnumebrs("reverse",[1,2,3,4])
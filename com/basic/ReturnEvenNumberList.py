def isEven(*args):
    list=[]
    for value in args:
        if value%2==0:
            list.append(value)
    return list

print(isEven(1,2,3,4,5,6))
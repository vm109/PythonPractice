def findSequenceInList(listOfNumbers,sequence):
    flag = False

    for i,v in enumerate(listOfNumbers):
        if v==int(sequence[0]) and i+1<len(listOfNumbers):
            if listOfNumbers[i+1] ==int(sequence[1])  and i+2<len(listOfNumbers):
                if listOfNumbers[i+2] == int(sequence[2]) :
                    flag = True
    return flag


print(findSequenceInList([1,2,3,0],"123"))
print(findSequenceInList([1,2,3,0,0,7],"007"))
print(findSequenceInList([1,2,3,0,0,7],"070"))


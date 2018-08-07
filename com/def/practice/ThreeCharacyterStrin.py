def createThreeCharacterString(stringInput):
    str=""
    for c in stringInput:
        c =c*3
        str=str+c
    return str


print(createThreeCharacterString("string"))
print(createThreeCharacterString("Mississipi"))
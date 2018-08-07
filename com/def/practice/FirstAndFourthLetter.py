def firstAndFourth(a):
    str=""
    i=0
    for c in a:
        if(i==0 or i==4):
            c=c.upper()
            print(c)
        i = i + 1
        str=str+c
    return str

print(firstAndFourth("helloworld"))
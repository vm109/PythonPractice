def reverseString(a):
    words=a.split(" ")
    i=len(words)
    str=""
    for x in range(-1,-i,-1):
        print(x)
        str = str+words[x]+" "
    str=str+" "+words[0]
    return  str


print(reverseString("hello world hi"))
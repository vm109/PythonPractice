def skyLine(str):
    i=0
    string=""
    for value in str:
        if i>0:
            if i%2==0:
                string=string+value.upper()
            else:
                 string=string+value.lower()
        else:
         string=string+value
        i+=1
    return string


print(skyLine("SkyliNesTrinGHI"))


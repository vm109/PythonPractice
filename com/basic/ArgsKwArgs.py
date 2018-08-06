# working with args and kwargs

def findAWordInkwArgs(word,**kwargs):
    for value in kwargs:
        if(kwargs[value] == word) :
            return True
        else :
            continue
    return False

print(findAWordInkwArgs("fruit",food="fruit",one="number"))
print(findAWordInkwArgs("meat",food="fruit",one="number"))
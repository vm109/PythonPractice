def pig_latin(word,endingword):
     if word[0] not in "aeiou":
         return word[1:]+word[0]+endingword
     else:
         return word+endingword

def looping(*args):
    for i,x in enumerate(args):
        print(i,x)

print(pig_latin("apple","ay"))
print(pig_latin("word","ay"))

looping(1,2,3,4)
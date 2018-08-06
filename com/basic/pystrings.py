str1 = "slicing and indexing with string"
def slice(x,y,z):
    ''' slice function takes starting index 'x', ending index 'y', and step value 'z','''
    print(str1[x:y:z])


def hello_name(name="world"):
    print("hello "+name)


result = hello_name("chicago")

print(type(result))


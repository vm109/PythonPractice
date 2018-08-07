def findSmallestAndLargest(a,b):
    greatest = a
    smallest = b
    if (a < b):
        greatest = b
        smallest = a
    if(a%2==0 and b%2==0):
       return smallest
    else:
        return greatest

print(findSmallestAndLargest(2,3))
print(findSmallestAndLargest(2,4))


def getPalindromeNumber(presentPalindrome,digitedNumber):
    arr=[]
    if digitedNumber==1 :
        if presentPalindrome<9 :
         arr.append(presentPalindrome+1)
         return arr
        else :
          arr.append(1)
          arr.append(1)
          return arr
    arr = convertToArray(presentPalindrome,digitedNumber)
    length = len(arr)
    mid = int(length/2)
    even = False
    if length % 2 == 0:
        even=True

    if(arr[mid]<9):
        arr[mid]= arr[mid]+1
        if even:
            arr[mid-1] = arr[mid-1]+1
    elif(arr[mid]==9):
        i = 0
        arr[mid] = 0
        if even:
            arr[mid-1] =  0
        while ((length-1)>mid+i):
             if(arr[mid+i+1] >=9 ):
                arr[mid+i+1] = 0
                if not even:
                 arr[mid-i-1] = 0
                else:
                 arr[mid-i-2] =0
                i=i+1
             else:
                 arr[mid + i + 1] = arr[mid + i + 1]+1
                 if not even:
                  arr[mid - i - 1] = arr[mid - i - 1]+1
                 else:
                  arr[mid-i-2] = arr[mid - i - 2]+1
                 break
    if(arr[0]==0 and arr[length-1]==0):
        arr[0]=1
        arr.append(1)
    return arr

def convertToArray(number,digitedNumber):
    arr = []
    while (digitedNumber!=0) :
     arr.append(int(number/(10**(digitedNumber-1))))
     number = int(number%(10**(digitedNumber-1)))
     digitedNumber = digitedNumber-1
    return arr


# def absoluteMinimum(number):
#     presentPalindrome, previousPalindrome = getPalindromeNumber(0,1)
#
#     while(presentPalindrome<number):
#         presentPalindrome,previousPalindrome = getPalindromeNumber(presentPalindrome,previousPalindrome)
#     return presentPalindrome
#
# print("test1 ",absoluteMinimum(9))



def generatePalindrome(minNumber):
    arr = getPalindromeNumber(-1, 1)
    number=0
    while (number<minNumber):
        number = 0
        i=0
        while(i<len(arr)):
            number = number+(arr[len(arr)-1-i]*(10**i))
            i= i+1
        arr = getPalindromeNumber(number,len(arr))
        print(number)

generatePalindrome(489)
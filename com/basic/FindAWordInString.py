def findWord(complete_string,word) :
    if word in complete_string :
        return True
    else :
        return False

print(findWord("this sentence has dog", "bear"))
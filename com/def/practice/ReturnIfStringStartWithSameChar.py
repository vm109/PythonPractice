def doesStringsHaveSameStartingChar(a):
    splitStrings = a.split(" ")
    return splitStrings[0][0].lower()==splitStrings[1][0].lower()

print(doesStringsHaveSameStartingChar("Hello How"))
print(doesStringsHaveSameStartingChar("Hello how"))
print(doesStringsHaveSameStartingChar("Hello Morning"))
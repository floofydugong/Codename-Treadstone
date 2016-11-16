def getCount(inputStr):
    return inputStr.count("a") + inputStr.count("e") + inputStr.count("i") + inputStr.count("o") + inputStr.count("u")

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
def toJadenCase(string):
    new_list = []
    split_strings = string.split()
    for i in split_strings:
        new_list.append(i[0].upper() + i[1:])
    print " ".join(new_list)

toJadenCase("How can mirrors be real if our eyes aren't real")

#ideas
# Prase through each and find a white space, then cap the next letter that follows?
# Break into a list, cap the first letter, then rejoin the whole list

'''
cool....capitalize just capitalizes the word
def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())

'''
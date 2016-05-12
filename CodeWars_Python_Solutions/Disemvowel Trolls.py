import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)


disemvowel("This website is for losers LOL!")

'''
another usage of translate to remove...notice it is not the removal of "aeiouAEIOU" but each letter in that
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

'''

'''
flag to ignore case is sick
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)
'''

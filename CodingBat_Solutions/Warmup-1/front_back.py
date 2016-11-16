'''

Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') -> 'eodc'
front_back('a') -> 'a'
front_back('ab') -> 'ba'

'''

def front_back(str):
    if len(str) == 0:
        return ('')
    elif len(str) == 1:
        return (str)
    elif len(str) == 2:
        first_letter = str[0]
        second_letter = str[1]
        return (second_letter + first_letter)
    else:
        first_letter = str[0]
        middle_stuff = str[1:len(str)-1:1]
        last_letter = str[len(str)-1]
        return (last_letter + middle_stuff + first_letter)
front_back('')
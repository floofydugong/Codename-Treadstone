'''

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') -> 'lloHe'
left2('java') -> 'vaja'
left2('Hi') -> 'Hi'

'''

def left2(str):
    print str[2:] + str[0:2] if len(str) > 2 else str

left2("Hello")
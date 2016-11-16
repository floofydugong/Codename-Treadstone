'''

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') -> 'Woo'
first_half('HelloThere') -> 'Hello'
first_half('abcdef') -> 'abc'

'''

def first_half(str):
    print str[:len(str)/2]

first_half("word")
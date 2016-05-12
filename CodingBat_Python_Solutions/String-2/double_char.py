'''

Given a string, return a string where for every char in the original, there are two chars.

double_char('The') -> 'TThhee'
double_char('AAbb') -> 'AAAAbbbb'
double_char('Hi-There') -> 'HHii--TThheerree'

'''

def double_char(str):
    new_list = []
    for i in str:
        new_list.append(i*2)
    print "".join(new_list)

double_char('word')
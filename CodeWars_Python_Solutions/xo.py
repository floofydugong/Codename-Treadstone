def xo(s):
    count_x = 0
    count_o = 0
    for i in s:
        if i.lower() == 'x':
            count_x += 1
        elif i.lower() == 'o':
            count_o += 1
        else:
            pass
    return (count_x == count_o)

xo('xxoo')

'''

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

'''
import math
def is_square(n):
    if n < 0:
        print False
    else:
        print (math.sqrt(n)%1 == 0)
is_square(4)


'''

from math import sqrt

def is_square(n):
    return n > 0 and sqrt(n).is_integer()

'''
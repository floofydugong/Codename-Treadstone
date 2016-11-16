'''

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) -> 4
make_chocolate(4, 1, 10) -> -1
make_chocolate(4, 1, 7) -> 2

'''
def make_chocolate(small, big, goal):
    #goal too large
    smalls_used = 0
    big_used = 0

    if goal > small * 1 + big * 5:
        return -1
    elif goal//5 >= big:
        big_used = big
        smalls_used = goal - big * 5
    else:
        big_used = goal//5
        smalls_used = goal - big_used * 5
        if smalls_used > small:
            return -1
    return smalls_used

'''
#Solution that worked but ran too long

def make_chocolate(small, big, goal):
    #goal too large
    smalls_used = 0
    big_used = 0

    if goal > small * 1 + big * 5:
        print -1
    else:
        while big_used * 5 + smalls_used < goal:
            if big_used < big:
                big_used += 1
            else:
                smalls_used += 1
    print smalls_used
'''




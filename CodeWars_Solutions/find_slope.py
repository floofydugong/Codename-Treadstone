'''

Given an array of 4 integers
[a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.

For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.

Assume that [a,b,c,d] and the answer are all integers (no floating numbers!). Slope:

'''

def find_slope(points):
    try:
        print str((points[3]-points[1])/(points[2]-points[0]))
    except Exception, e:
        print "undefined"

find_slope([10,50,30,150])

'''
Forgot that you can unpack...

def find_slope(points):
    a,b,c,d = points
    return 'undefined' if a == c else str((b - d) / (a - c))

'''

def next_id(arr):
    if not arr or 0 not in arr:
        print 0
    else:
        for i in range(min(arr),max(arr)+1):
            if i+1 not in arr:
                print i+1
                break

next_id([0,1,2,4,5])

#sort them and then do the plus one for loop?
#if not in range, print to array pick min?

'''

def next_id(arr):
    t = 0
    while t in arr:
        t +=1
    return t

'''
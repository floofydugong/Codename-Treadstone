def unused_digits(*l):
    #neat....set will literally break down each of chars into it's own thing
    digits_set = set(list("0123456789"))
    test_set = set("".join(str(i) for i in l))
    d = digits_set.difference(test_set)
    r = "".join(sorted(d))
    print r

unused_digits((12, 34, 56, 78)) #"09"

'''
def unused_digits(*args):
    bad_string = ""
    answer = ""

    for i in args:
        bad_string += str(i)

    for x in range(0,10):
        if str(x) not in list(bad_string):
            answer += str(x)
    print answer

unused_digits((12, 34, 56, 78)) #"09"

#split the numbers and set, see what is not in master set

'''

'''
# some next level usage of translate
def unused_digits(*args):
    return "0123456789".translate(None,''.join([str(i) for i in args]))

'''


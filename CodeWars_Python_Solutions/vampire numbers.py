def vampire_test(x, y):
    print sorted(str(x)+str(y)) == sorted(str(x*y))

#notes:
#sorted automatically converts to a list...cool

# def vampire_test(x, y):
#     print sorted(str(x * y)) == sorted(str(x) + str(y))


vampire_test(-246,-510)
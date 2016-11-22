def arr_check(arr):
    print (all(isinstance(i,list)for i in arr))
arr_check([['A']])
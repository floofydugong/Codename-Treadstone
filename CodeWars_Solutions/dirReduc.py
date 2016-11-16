def dirReduc(arr):
    redundant_dir = ['WESTEAST','EASTWEST','NORTHSOUTH','SOUTHNORTH']
    restart = True

    while restart:
        restart = False
        for i in range(0,len(arr)-1):
            if arr[i]+arr[i+1] in redundant_dir:
                arr.pop(i+1)
                arr.pop(i)
                restart = True
                break
    return arr
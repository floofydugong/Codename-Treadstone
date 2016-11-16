def length_of_sequence(arr,n):
    new_list = []
    [new_list.append(i) for i in range(len(arr)) if arr.count(n) == 2 and arr[i] == n]
    try:
        return new_list[1]-new_list[0] + 1
    except Exception, e:
        return 0

length_of_sequence([1,1],1)


#Don't forget that you can start/end at certain places . Notice the usage of a+1 to start of ahead of "a"
def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    a = arr.index(n)
    b = arr.index(n, a + 1)
    return b - a + 1
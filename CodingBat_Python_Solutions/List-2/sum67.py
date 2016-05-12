'''


Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) -> 5
sum67([1, 2, 2, 6, 99, 99, 7]) -> 5
sum67([1, 1, 6, 7, 2]) -> 4

'''

def sum67(nums):
    dontadd = 0
    sum = 0
    for i in range(len(nums)):
        if dontadd == 0:
            if nums[i] == 6:
                dontadd = 1
            else:
                sum += nums[i]
        else:
            if nums[i] == 7:
                dontadd = 0
            else:
                pass
    print sum


sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])



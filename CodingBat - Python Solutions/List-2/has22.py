'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) -> True
has22([1, 2, 1, 2]) -> False
has22([2, 1, 2]) -> False

'''

def has22(nums):
    count = 0
    if 2 not in nums:
        print False
    else:
        for i in range(len(nums)):
            if nums[i] == 2 and i+1 < len(nums) and nums[i+1] == 2:
                count =+ 1
            else:
                pass

    print (count > 0)

has22([1,2,2,2])
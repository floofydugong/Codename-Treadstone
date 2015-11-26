'''

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) -> 6
sum13([1, 1]) -> 2
sum13([1, 2, 2, 1, 13]) -> 6

'''

def sum13(nums):
    if 13 not in nums:
        print sum(nums)
    else:
        for i in nums:
            try:
                nums[nums.index(13)+1] = 0
            except Exception, e:
                pass
            try:
                nums[nums.index(13)] = 0
            except Exception, e:
                pass
        print sum(nums)

sum13([1, 2, 13, 2, 1, 13,1])

'''

def sum13(nums):
  if len(nums) == 0:
    return 0

  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums):
        nums[i+1] = 0
  return sum(nums)

'''

'''

Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

array123([1, 1, 2, 3, 1]) -> True
array123([1, 1, 2, 4, 1]) -> False
array123([1, 1, 2, 1, 2, 3]) -> True

'''

def array123(nums):
    if not nums:
        print False
    for i, value in enumerate(nums):
        try:
            if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                print True
                break
        except Exception, e:
            #this seems to default correctly...lol
            print False

array123([])

'''
def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
'''


'''
#Solution cannot use imports...
import re

def array123(nums):
    string_nums = ""
    for i in nums:
        string_nums = string_nums + str(i)
    print string_nums

    if re.findall("123", string_nums):
        print True
    else:
        print False
'''




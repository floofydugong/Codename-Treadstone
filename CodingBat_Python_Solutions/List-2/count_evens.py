'''

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) -> 3
count_evens([2, 2, 0]) -> 3
count_evens([1, 3, 5]) -> 0

'''


#modulus expects a return, so true if odd
def count_evens(nums):
    counter = 0
    for i in nums:
        if not i%2:
            counter += 1
    print counter

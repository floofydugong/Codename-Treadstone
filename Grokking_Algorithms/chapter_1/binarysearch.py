"""
Notes:
- Python2 rounds down, so (1+2)/2 = 1
- Interestingly enough, if you let it round, it will loop through 3 times (2,0,1). It goes to zero because (0+1)/2 = 0
    - Low = 0, High = 1
- Must cast part of it as a float
"""
import math

def binary_search (num_list, item):
    low = 0
    # minus 1 since list indexes start at 0
    high = len(num_list)- 1

    while low <= high:
        mid = int(math.ceil(float(low)/high))
        print(mid)
        guess = num_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid +1
    return None

num_list = [1,3,5,7,9]

print binary_search(num_list, 3) # => 1
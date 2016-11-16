'''

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) -> [2, 3, 1]
rotate_left3([5, 11, 9]) -> [11, 9, 5]
rotate_left3([7, 0, 0]) -> [0, 0, 7]

'''

def rotate_left3(nums):
    new_list = []
    new_list.append(nums[-2])
    new_list.append(nums[-1])
    new_list.append(nums[-3])

    print new_list

rotate_left3([1,2,3])
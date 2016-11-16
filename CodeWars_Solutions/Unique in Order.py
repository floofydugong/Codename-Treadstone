# def unique_in_order(iterable):
#     new_list = []
#     if iterable:
#         for i in range(0,len(iterable)-1):
#             if iterable[i] == iterable[i+1]:
#                 pass
#             else:
#                 new_list.append(iterable[i])
#         new_list.append(iterable[-1])
#     print new_list

def unique_in_order(iterable):
    new_list = []
    prev = None

    for char in iterable:
        if char != prev:
            new_list.append(char)
            prev = char
    print new_list

unique_in_order('AAAABBBCCDAABBB')


# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     print result

# unique_in_order('AAAABBBCCDAABBB')

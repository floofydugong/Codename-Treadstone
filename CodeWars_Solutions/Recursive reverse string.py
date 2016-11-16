def reverse(str):
    x = 0
    count = 0
    new_list = []
    max_length = len(str)

    for i in range(len(str)):
        count += 1
        new_list.insert(x, str[i])
        x -= 1
    print "".join(new_list)
    print count

reverse("1234")


'''
def reverse(str):
  return str[-1] + reverse(str[:-1]) if len(str) > 1 else str

'''
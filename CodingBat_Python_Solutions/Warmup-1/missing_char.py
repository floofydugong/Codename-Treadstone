'''

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) -> 'ktten'
missing_char('kitten', 0) -> 'itten'
missing_char('kitten', 4) -> 'kittn'

'''

def missing_char(str, n):
    new_list = list(str)
    best_list = []
    new_list[n] = ''
    for i in new_list:
        if i != '':
            best_list.append(i)
    x = "".join(best_list)
    return (x)

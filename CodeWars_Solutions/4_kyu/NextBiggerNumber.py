from itertools import permutations

def next_bigger(n):

    num_list = list(str(n))

    max_length = (len(num_list)) * -1
    tail_cutoff = -2

    if len(num_list) <= 2:
        reverse_num = int(''.join(num_list[::-1]))
        return(reverse_num if reverse_num > n else -1)

    while tail_cutoff >= max_length:

        head_value = num_list[:tail_cutoff]
        tail_values = num_list[tail_cutoff:]

        tail_perms = list(permutations(tail_values))

        answer_list = [int(''.join(head_value)+''.join(i)) for i in tail_perms]

        greater_than_n = list(filter(lambda x: x > n, answer_list))

        if greater_than_n and min(greater_than_n) > n:
            return(min(greater_than_n))
        else:
            tail_cutoff-=1
    return(-1)

next_bigger(144)
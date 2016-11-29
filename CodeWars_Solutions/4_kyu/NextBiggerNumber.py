def next_bigger(n):

    num_list = str(n)

    curr_idx = len(num_list) -1

    while curr_idx >= 1:
        if num_list[curr_idx] > num_list[curr_idx-1]:
            head_list = num_list[:curr_idx-1]
            switch_list = [int(i) for i in num_list[curr_idx-1:]]

            val_to_beat= num_list[curr_idx-1]

            set_list = sorted(list(set(switch_list)))

            for val in set_list:
                if val > int(val_to_beat):
                    new_start_val =  val
                    break

            sort_switch_list = sorted(switch_list)
            sort_switch_list.remove(new_start_val)

            sort_switch_list = ''.join(str(x) for x in sort_switch_list)

            return(int(head_list+str(new_start_val)+sort_switch_list))
        else:
            curr_idx -= 1
    return(-1)

next_bigger(12)


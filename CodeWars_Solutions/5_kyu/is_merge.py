def is_merge(s, part1, part2):
    # idea is to pop

    part1 = list(part1)
    part2 = list(part2)

    for index,value in enumerate(s):
        try:
            if part1 and value in part1[0]:
                del part1[0]
            elif value in part2[0]:
                del part2[0]
            else:
                return(False)
        except:
            return(False)
    return(True)

is_merge('codewars','cod','wars')
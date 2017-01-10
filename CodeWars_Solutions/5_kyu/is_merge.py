def is_merge(s, part1, part2):
    part1 = list(part1)
    part2 = list(part2)


    for char in s:
        if part1 and char == part1[0]:
            del part1[0]
        elif part2 and char == part2[0]:
            del part2[0]
        else:
            return(False)
    return(part1 == part2)



is_merge('codewars','cod','wars')
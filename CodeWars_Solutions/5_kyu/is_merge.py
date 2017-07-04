# recursion problem

def is_merge(s, part1, part2):
    # return (s == part1 + part2 if not (s and part1 and part2) else
    #     s[0] == part1[0] and is_merge(s[1:], part1[1:], part2) or
    #     s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]))

    if not (s and part1 and part2):
      return(s == part1 + part2)
    else:
      return(s[0] == part1[0] and is_merge(s[1:], part1[1:], part2) or
        s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]))

is_merge('ananas','ana','nas')
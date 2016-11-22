def scramble(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    s1_index = 0
    s2_index = 0

    while s1_index < len(s1):
        if s2_index == len(s2) -1:
            return(True)
        if s1[s1_index] == s2[s2_index]:
            s1_index +=1
            s2_index +=1
        else:
            s1_index +=1
    return(False)

scramble('cedewaraaossoqqyt','codewars')
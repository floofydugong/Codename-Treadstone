def pattern(n):
    new_list = []
    string = ""
    if n == 1:
        return '1'
    elif n < 1:
        return ""
    else:
        while n >= 1:
            string = str(string) + str(n)
            n -= 1
            new_list.append(string)
        new_list.reverse()
    return "\n".join(new_list)

pattern(5)


def pattern(n):
    return "\n".join(["".join([str(y) for y in range(n, x, -1)]) for x in range(n)]);


def pattern(n):
    return "\n".join(["".join([str(y)] for y in range(n, x, -1)) for x in range(n)]);
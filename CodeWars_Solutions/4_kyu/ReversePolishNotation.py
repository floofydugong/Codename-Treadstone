def calc(expr):
    stack = []
    float_num = False

    if not expr:
        return(0)

    split_expr = expr.split()

    for char in split_expr:
        if str.isdigit(char):
            stack.append(int(char))
        elif '.' in char:
            stack.append(float(char))
            float_num = True
        else:
            first_val = str((stack.pop(-2)))
            second_val = str((stack.pop(-1)))

            if float_num:
                new_val = eval(first_val+char+second_val)
            else:
                new_val = int(eval(first_val+char+second_val))
            stack.append(str(new_val))

    if float_num:
        return(float(stack[-1]))
    else:
        return(int(stack[-1]))

calc("4 2 /")


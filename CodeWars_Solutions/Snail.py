def snail(array):

    answer = []
    while len(array)>=1:

        # Top Layer
        answer.extend(array.pop(0))

        try:
            # Right Side
            for i in array:
                answer.append(i.pop(-1))

            # Bottom Layer
            bot_layer = array.pop(-1)
            reverse_bot_layer = list(reversed(bot_layer))
            answer.extend(reverse_bot_layer)

            # Left Side
            left_layer = [i.pop(0) for i in array]
            answer.extend(left_layer[::-1])
        except:
            pass

    return(answer)

snail([[1,2,3],
       [4,5,6],
       [7,8,9]]
import re

def dashatize(num):

    if num == None:
        return  ('None')

    str_num = list(str(num).replace('-',''))
    answer = [str_num[i] if int(str_num[i]) % 2 ==0 and int(str_num[i+1]) % 2 == 0 else str_num[i]+'-' for i in range(len(str_num)-1)]

    answer.append(str_num[-1])

    print (''.join(answer))

dashatize(2344)
# def make_readable(seconds):
#     times = [("hour", 60 * 60),
#              ("minute", 60),
#              ("second", 1)]

#     answer = []

#     for time,time_secs in times:
#         qty = seconds//time_secs
#         answer.append('0'+str(qty) if qty < 10 else str(qty))
#         seconds = seconds % time_secs
#     print(":".join(answer))

def make_readable(s):
    print ('{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60))

make_readable(86399)
def get_sum(a,b):
    return a if a==b else sum (i for i in range(min(a,b),max(a,b)+1))


get_sum(1,2)
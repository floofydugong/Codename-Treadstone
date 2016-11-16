def triangular(n):
    return 0 if n < 0 else (n**2 + n)/2

# This solution worked...but too too much memory...a quick google shows that you can calculate using above formula
# def triangular(n):
#     return sum([i for i in range(n+1)])

triangular(10)
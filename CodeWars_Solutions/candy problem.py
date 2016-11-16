def candies(s):
    print - 1 if not s or len(s) == 1 else max(s)*(len(s)-1) - (sum(s)-max(s))

candies([5,8,6,4])
def pattern(n):
    print "\n".join([str(n) * n for n in range(1,n+1)])

pattern(2)

# def pattern2(n):
#     print "\n".join(["".join([str(y) for y in range(n, x, -1)]) for x in range(n)]);
# pattern2(2)
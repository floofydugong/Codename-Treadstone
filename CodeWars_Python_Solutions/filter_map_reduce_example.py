def f (x): return x**2

print f(8)
64

g = lambda x: x**2

print g(8)
64

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)
44 48

print make_incrementor(22)(33)
55

foo = [2,18,9,22,17,24,8,12,27]

print filter(lambda x: x % 3 == 0, foo)
[18,9,24,12,27]

print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]

print reduce(lambda x,y: x + y, foo)
139

# returns range from 2 to 49
nums = range (2,50)
for i in range (2,8):
    nums = filter(lambda x: x == i or x % i, nums)

print nums


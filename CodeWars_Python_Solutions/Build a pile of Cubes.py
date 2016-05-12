def find_nb(m):
  total, i = 1, 2
  while total < m:
    total += i * i * i
    i += 1
  return i - 1 if total == m else -1

#Why did this one perform better? Basicallys same logic?
#No sum for a for loop...


# Solution worked but timed out
def find_nb(m):
    total = 0
    finish = False
    start = 2

    while total < m :
        total = sum([i**3 for i in range(1,start)]) #this is too fancy. Think more simple next time
        start += 1
    print start-2 if total == m else -1


find_nb(4183059834009)
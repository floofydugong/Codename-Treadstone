def collatz(n):
    count = 1
    while n != 1:
        if not n%2: #even
            n = n/2
        else:
            n = n * 3 +1
        count += 1
    return count

collatz(20)
def hamming_distance(a, b):
    count = 0
    string_a = str(a)
    string_b = str(b)

    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            count += 1
    print count

hamming_distance(1234,4321)

'''
#Alternative Solution

def hamming_distance(a, b):
    return sum(c != d for c, d in zip(a, b))


'''
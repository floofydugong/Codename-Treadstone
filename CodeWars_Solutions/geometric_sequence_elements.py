def geometric_sequence_elements(a, r, n):
    star_val = [a]
    final_answer = str(a)
    for values in range(0,4):
        start_val =start_val*r
        final_answer += ',' + str(list_of_values[-1])
    print (final_answer)

geometric_sequence_elements(2,3,5)

def geometric_sequence_elements(a, r, n):
    return ', '.join(str(a * r ** i) for i in xrange(n))
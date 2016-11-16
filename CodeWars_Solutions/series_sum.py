def series_sum(n):
    counter = 1
    total = 0
    increase_value = 1
    if n == 0:
        return "%.2f" % float(0.00)
    else:
        while n >= counter:
            print increase_value
            total += float(1/float(increase_value))
            increase_value += 3
            counter += 1
    print "%.2f" % float(total)



#automatically returns zero if it cannot iterate through range
#format decimals to two decimal places
def series_sum(n):
    print '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

series_sum(0)
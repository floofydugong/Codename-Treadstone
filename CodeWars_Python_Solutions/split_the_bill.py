def split_the_bill(x):
    total_sum = 0
    length = 0
    new_dict = {}

    for key, value in x.iteritems():
        total_sum += float("{:.2f}".format(value))
        length += 1

    for key in x:
        new_dict[key] = round(x[key] - total_sum/float(length),2)

    print new_dict

split_the_bill(
    {
    'A': 20,
    'B': 15,
    'C': 10
    }
)

'''

split_the_bill=lambda x: (lambda avg: {a: round(x[a]-avg,2) for a in x})(1.0*sum(x.values())/len(x))

'''

'''

def split_the_bill(x):
    diff = sum(x.values())/float(len(x))
    return {k: round(x[k]-diff, 2) for k in x}

'''
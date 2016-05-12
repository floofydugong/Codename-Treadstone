def number(bus_stops):
    total = 0
    for i in bus_stops:
        total = total + i[0] - i[1]
    print total

'''

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


'''
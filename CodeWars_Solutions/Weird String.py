def to_weird_case(string):
    counter = 0
    list_string = list(string)
    for i in range(len(list_string)):
        if list_string[i] == " ":
            counter = 0
            continue
        counter += 1
        if counter%2:
            list_string[i] = string[i].capitalize()

    print "".join(list_string)

to_weird_case('This is a test')

#to_weird_case('String'); # => returns 'StRiNg'
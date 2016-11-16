def is_isogram(string):
    lower_string = string.lower()
    print (len(set(lower_string)) == len(lower_string))

is_isogram("aba")

'''
#lambda usage

is_isogram = lambda s: len(set(s.lower())) == len(s)

'''
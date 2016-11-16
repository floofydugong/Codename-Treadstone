def my_parse_int(string):
    new_string =  string.strip()
    if new_string.isdigit():
        return int(new_string)
    else:
        return "NaN"

my_parse_int("1 1")

'''
strips removes whitespaces from the end
replace removes all whites spaces
alternatively, splitting and joining can achieve the same thing


def first_non_repeating_letter(string):
    lower_str = string.lower()

    for index, letter in enumerate(lower_str):
        if lower_str.count(letter) == 1:
            return(string[index])
    return('')

first_non_repeating_letter('')
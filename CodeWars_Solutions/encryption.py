#CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    return ' '.join([' ' if letter == ' ' else CHAR_TO_MORSE[letter] for letter in string])
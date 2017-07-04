# https://www.codewars.com/kata/simple-fun-number-176-reverse-letter/train/python

def reverse_letter(string):
    print (''.join([l for l in string[::-1] if l.isalpha()]))
reverse_letter('hello123')
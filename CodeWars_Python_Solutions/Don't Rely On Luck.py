from random import randint

def function(guess,lucky_number):
    while guess != lucky_number:
        lucky_number = randint(1,100)
        print lucky_number

function(1,randint(1,100))
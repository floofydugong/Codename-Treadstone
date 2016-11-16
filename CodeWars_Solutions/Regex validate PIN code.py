def validate_pin(pin):
    return (pin.isdigit() and len(pin) in [4,6])

validate_pin("1234")

'''

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()

'''

from re import match
def validate_pin(pin): return match(r'^(\d{4}|\d{6})$', pin) != None


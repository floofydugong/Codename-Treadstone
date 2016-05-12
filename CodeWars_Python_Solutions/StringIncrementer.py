'''
#Solution Breakdown

The method zfill() pads string on the left with zeros to fill width.

'''

import re

def increment_string(input):
   #\d* = one or more digits, $ symbolizes at the end
    match = re.search("(\d*)$", input)
    if match:
      # matches the first regular expression group
        number = match.group(0)
        if number is not "":
            #Because these are both returns, the function will exit on the first return
            #The first part of the code returns all the letters without the numbers
            #The second portition returns the number + 1, and then fills in the missing zeroes if necessary
            print input[:-len(number)] + str(int(number) + 1).zfill(len(number))
    print input + "1"

increment_string("foobar098")
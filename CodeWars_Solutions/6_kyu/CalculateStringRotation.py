# https://www.codewars.com/kata/calculate-string-rotation/train/python

def shifted_diff(first, second):
    for i in range(0,len(second)):
       print (second[0]+second[0:-i])
       # print (True if second[-i]+second[0:-1] == first else False)



shifted_diff('fatigue','tiguefa')


# "coffee", "eecoff" => 2
# "eecoff", "coffee" => 4
# "moose", "Moose" => -1
# "isn't", "'tisn" => 2
# "Esham", "Esham" => 0
# "dog", "god" => -1
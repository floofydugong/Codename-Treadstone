def openOrSenior(data):

    answer = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            answer.append("Senior")
        else:
           answer.append("Open")
    print answer

openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])


'''
#notice how the answer is in list form already...
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]

'''

'''
#map takes a function and applies to all things in the dataset given
#read a map backwards...
#for every x in data, apply rule
def openOrSenior(data):
  return map(lambda x: 'Senior' if x[0] >= 55 and x[1] > 7 else 'Open', data)

'''
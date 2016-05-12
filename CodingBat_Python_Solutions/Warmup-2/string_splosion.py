'''

Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') -> 'CCoCodCode'
string_splosion('abc') -> 'aababc'
string_splosion('ab') -> 'aab'

'''

def string_splosion(str):
    x = len(str)
    final_word =[]
    while x >= 0:
        word = str[0:x:1]
        final_word.insert(0,word)
        x -= 1
    return "".join(final_word)

string_splosion("word")


'''

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

'''

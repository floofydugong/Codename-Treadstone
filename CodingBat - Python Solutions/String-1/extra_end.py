'''Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') -> 'lololo'
extra_end('ab') -> 'ababab'
extra_end('Hi') -> 'HiHiHi'

'''

def extra_end(str):
    print (str[-2]+str[-1])*3

extra_end("word")

'''
#Alternative solution

def extra_end(str):
  end = str[-2:]
  return end + end + end

'''
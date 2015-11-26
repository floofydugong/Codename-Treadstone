'''

Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') -> True
end_other('AbC', 'HiaBc') -> True
end_other('abc', 'abXabc') -> True

'''

def end_other(a, b):
    lower_a = a.lower()
    lower_b = b.lower()

    len_a = len(lower_a)
    len_b = len(lower_b)

    return(lower_a[-1*len_b:] == lower_b or lower_b[-1*len_a:] == lower_a)

end_other("abc","abXabc")

'''
#endswith...
Solution:

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

'''
def count_arara(n):
   num_of_adak = n//2
   word_return = ''
   i = 0

   if not n%2: #case of even
      while i < num_of_adak-1:
         word_return = word_return + 'adak '
         i = i+1
      word_return= word_return + 'adak'
      print word_return
   else: # case of odd
      while i < num_of_adak:
         word_return = word_return + 'adak '
         i = i+1
      word_return= word_return + 'anane'
      print word_return

# highest best practice answer
# def count_arara(n):

#     print ' '.join(['adak'] * (n / 2) + ['anane'] * (n % 2))

'''
Used the ".join" to concatante spaces and the words adak or anane.
adak can only be returned if n was even. (floor division occurs on integers). 3/2 returned 1
anane can only be returned when odd (returns the modulus. For 3/2, it would return 1)
3 would correctly return "adak anane"
'''

count_arara(1)

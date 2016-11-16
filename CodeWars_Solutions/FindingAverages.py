def average(x):
   if type(x) is str or not x:
      print "Incorrect";
   elif len(x) == 1:
      print x[0]
   else:
      print sum(x)/len(x)

average([305])
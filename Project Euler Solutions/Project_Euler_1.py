#Project Euler: Problem 1 Solution

def check_mod_3_5():
   "This function will take an input and check if the MOD 3 or MOD 5 of that value returns 0"

   number = 0;

   for i in range(1000):
      if i % 3 == 0 or i % 5 == 0:
         number = number +i
   print number

check_mod_3_5();
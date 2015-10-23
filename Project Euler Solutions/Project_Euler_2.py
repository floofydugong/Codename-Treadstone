#Project Euler: Problem 2 Solution

def fibonnaci_sequence_sum():
   total = 0;
   answer = 0;
   prev_num = 0;
   curr_num = 1;

   while total < 4000000:
      total = curr_num + prev_num;
      prev_num = curr_num;
      curr_num = total;
      if total % 2 == 0:
         answer = answer + total;
   print total
   print answer

fibonnaci_sequence_sum();
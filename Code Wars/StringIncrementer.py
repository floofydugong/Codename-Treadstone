import re

def increment_string(strng):
   if strng == "":
      print "1"
   elif str.isalpha(strng):
      print str(str(strng)+"1");
   elif str.isdigit(strng):
      orig_number_len = len(strng);

      number_p_one = str(int(strng)+1)
      number_p_one_len = len(str(number_p_one))

      if number_p_one_len >= orig_number_len:
         print number_p_one
      else:
         pad_len = number_p_one_len;
         pad_num = number_p_one;
         while pad_len < orig_number_len:
            pad_num = str("0"+str(pad_num))
            pad_len = len(pad_num)
         print pad_num
   elif not str.isalpha(strng):
      orig_number = re.split(r"\D+",strng);
      orig_number_len = len(orig_number[1]);

      number_p_one = int(orig_number[1]) + 1;
      number_p_one_len = len(str(number_p_one));

      if number_p_one_len >= orig_number_len:
         print re.search(r"[^0-9]+",str(strng)).group(0)+str(number_p_one);
      elif number_p_one_len < orig_number_len:
         pad_len = number_p_one_len;
         pad_num = number_p_one;
         while pad_len < orig_number_len:
            pad_num = "0"+str(pad_num)
            pad_len = len(pad_num)
         print re.search(r"[^0-9]+",str(strng)).group(0) + pad_num

increment_string('O520395y6IK496345622eM16138^"WV64134283k}3< 0>67053976j6+j3nj l78672241501108389')
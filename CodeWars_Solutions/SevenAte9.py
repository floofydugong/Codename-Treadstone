'''

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'

'''

def seven_ate9(str_):
    strung_out = str_
    for i in range(len(strung_out)):
        if strung_out[i:i+3] == '797':
            strung_out = strung_out.replace('797','77')
        else:
            pass
    return strung_out

seven_ate9('79797')

'''

def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_

def seven_ate9(str_):
    return str_.replace('797','77').replace('797', '77')

'''
'''

Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') -> True
xyz_there('abc.xyz') -> False
xyz_there('xyz.abc') -> True

'''

def xyz_there(str):
    count = 0
    for i in range(len(str)-2):
        print str[i:i+3]
        if str[i:i+3] == 'xyz' and str[i-1:i+3] != '.xyz':
            count += 1
    print (count > 0)

xyz_there('abc.xyz')
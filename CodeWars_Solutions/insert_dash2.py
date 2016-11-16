'''
Write a function insertDashII(num) that will insert dashes ('-')
between each two odd numbers and asterisk ('*') between each even numbers in num

notes:

continue/breaks are used to increase performance
'''

def insert_dash2(num):
    #converting number to a list to iterate through
    num = list(str(num))
    answer = ''
    #enumerate assigns an index to each of the items in the list
    for index, obj in enumerate(num):
        previous = num[index - 1]
        #skips the first index and continues to next value. The continue restarts the whole process with the next value
        if (index==0)or(int(obj)==0)or(int(previous)==0):
            answer += obj
            continue
            #this continue prevents the answer from being returned unless it makes it into the elsifs
            #continue
        elif (int(obj)%2==0 and int(previous)%2==0):
            answer += '*'+ obj
        elif (int(obj)%2!=0 and int(previous)%2!=0):
            answer += '-' + obj
        else:
            #handles cases of odd/even and even/odd
            answer += obj
    return answer


#notes
#int() checks for values greatet than zero...
#the "string"[] trick below is smart...

def insert_dash2(num):

    prev = 0
    out = ''

    for dig in str(num):
        if int(dig) % 2 == int(prev) % 2 and int(prev) and int(dig):
            out += '*-'[int(prev) % 2]
        out += dig
        prev = dig
    print out

insert_dash2(11203346)
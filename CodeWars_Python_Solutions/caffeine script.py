'''Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".

If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"'''

def caffeineBuzz(n):

    answer = "mocha_missing!"

    if not n%3 and not n%4:
        answer = "Coffee"
    elif not n%3:
        answer = 'Java'

    if not n%2 :
        answer += "Script"

    print answer

caffeineBuzz(12)
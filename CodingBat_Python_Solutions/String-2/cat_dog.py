'''

Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') -> True
cat_dog('catcat') -> False
cat_dog('1cat1cadodog') -> True

'''

def cat_dog(str):
    cat_counter = 0
    dog_counter = 0
    for i in range(len(str)):
        if str[i:i+3] == 'cat':
            cat_counter += 1
        elif str[i:i+3] == 'dog':
            dog_counter += 1
    print (cat_counter == dog_counter)

cat_dog("ca")


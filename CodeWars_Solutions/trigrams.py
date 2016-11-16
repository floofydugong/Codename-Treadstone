def trigrams(phrase):

    x = 0
    final_list = []

    if len(phrase) <= 3:
        print ''
    else:
        while x < len(phrase) - 2:
            y = x + 1
            z = y + 1
            trigram = str(phrase[x] + phrase[y] + phrase[z]).replace(' ','_')
            final_list.append(trigram)
            x = x + 1
        print ' '.join(final_list)

trigrams("the quick red")


# def trigrams(phrase):
#     phrase = phrase.replace(" ", "_")
#     return " ".join([phrase[i:i+3]for i in range(len(phrase)-2)])

'''
Best Answer Analysis Notes:
- Begins by replacing white spaces with underscore
- Then proceeds to use the " ".join move to add letters in the range (only one value, which is the stop value)

'''
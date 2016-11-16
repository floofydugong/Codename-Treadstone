import re

#when a dictionary sorts, its really dumb. It takes numbers first, then upper case alphabetically, then lower case alphabetically

def order(sentence):

    answer = {}

    for i in sentence.split():
        answer[(re.search(r'\d', i)).group(0)] = i
    print " ".join([answer[i] for i in sorted(answer)])
    print answer
    print sorted(answer.values(), key = lambda x: sorted(x))
    print sorted(answer.values(), key = lambda x: x)


order("is2 Thi1s T4est 3a")

#ideas
#dictionary?

def order(words):
  print ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

#order("is2 Thi1s T4est 3a")

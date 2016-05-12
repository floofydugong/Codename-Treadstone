def DNA_strand(dna):
    new_string = ""
    for i in dna:
        new_string += ({"A":"T", "T":"A", "C":"G", "G":"C"}.get(i))
    print new_string

DNA_strand("TAACG")

'''
DNA_strand = lambda dna: "".join([{"A":"T","T":"A","C":"G","G":"C"}[i] for i in dna])
'''

'''

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

'''
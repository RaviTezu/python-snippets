#!/usr/bin/python
""" This scirpt genrates all the possbile english from a word """
import sys
import itertools
try:
    import enchant
except:
    print "You should have enchant module installed to run this script: pip install pyenchant works!"
    sys.exit(1)


def combs(word,l):
    for i in itertools.permutations(word,l):
        current_word = str("".join(i))
        if d.check(current_word):
            if not current_word in sequences:
                sequences.append(current_word)


if __name__ == "__main__":

    word = str(raw_input("Please enter a word: "))
    if word.isalpha():
        sequences = []
        d = enchant.Dict("en_US")
        word_len = len(word)
        word_list = list(word)
        print "Generating all possible words..."
        while word_len > 2:
            combs(word_list,word_len)
            word_len = word_len - 1
        print sequences
    else:
        print "WTF? Check what you've entered!"

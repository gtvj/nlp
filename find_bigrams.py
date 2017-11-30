import nltk
from nltk.collocations import *

def get_bigrams(words):

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationFinder.from_words(words)

    return sorted(finder.ngram_fd.items())
import nltk
from nltk.collocations import *

def get_bigrams(words):

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationFinder.from_words(words)

    finder.apply_freq_filter(3) # Restrict bigrams to those that appear at least three times

    return sorted(finder.ngram_fd.items())
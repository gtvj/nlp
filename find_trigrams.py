import nltk
from nltk.collocations import *

def get_trigrams(words):

    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    finder = TrigramCollocationFinder.from_words(words)

    finder.apply_freq_filter(4) # Restrict trigrams to those that appear at least three times

    return sorted(finder.ngram_fd.items())
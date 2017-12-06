import nltk
from nltk import TrigramCollocationFinder, BigramCollocationFinder


def get_trigrams(words):

    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    finder = TrigramCollocationFinder.from_words(words)

    finder.apply_freq_filter(3) # Restrict trigrams to those that appear at least three times

    return sorted(finder.ngram_fd.items())


def get_bigrams(words):

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationFinder.from_words(words)

    finder.apply_freq_filter(4) # Restrict bigrams to those that appear at least three times

    return sorted(finder.ngram_fd.items())


def find_ngram_match(ngram, decorated_guides, type):

    ngrams = []

    for ngram_in_details in ngram:
        sorted_ngram = sorted(list(ngram_in_details[0]))

        for guide in decorated_guides:
            for item in guide[type]:
                if sorted_ngram in item:
                    ngrams.append(' '.join(str(e) for e in sorted_ngram) + ' found in ' + guide['guide_href'])

    return ngrams
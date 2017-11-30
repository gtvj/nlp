from nltk.tokenize import word_tokenize, sent_tokenize


def tokenize(text):
    sents = sent_tokenize(text)
    words = [word_tokenize(sent) for sent in sents]
    return words

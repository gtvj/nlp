from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_to_words(text):
    words = word_tokenize(text)
    return words

def tokenize_to_sentences(text):
    sentences = sent_tokenize(text)
    return sentences
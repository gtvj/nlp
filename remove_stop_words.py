from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize


def remove_stopwords(text):
    custom_stopwords = set(stopwords.words('english') + list(punctuation))

    words_without_stopwords = ' '.join([word for word in word_tokenize(text) if word not in custom_stopwords])

    return words_without_stopwords

from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize
import re


def extract_words_without_stopwords(text):

    my_stopwords = ['...', '+44', '\-', '\'s', 'The']

    custom_stopwords = set(stopwords.words('english') + list(punctuation) + my_stopwords)

    words_without_stopwords = ' '.join([word for word in word_tokenize(text) if word not in custom_stopwords])

    words_without_stopwords_or_dates = re.sub('\d{1,4}', ' ', words_without_stopwords).strip()

    return words_without_stopwords_or_dates

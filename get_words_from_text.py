from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize
import re


def extract_words_without_stopwords(text):
    my_stopwords = ['...', '+44', '\-', '\'s', 'The', 'catalogue', 'records', 'National Archives', 'available', 'view', 'online', 'series', 'advanced', 'see section']

    my_patterns = ['-', '/', u'\u2013', u'\u2018', u'\u2019', u'\xa3', u'\u201c', u'\u201d', '[Ss]earch', '[Dd]iscovery' ]

    custom_stopwords = set(stopwords.words('english') + list(punctuation) + my_stopwords)

    words_without_stopwords = ' '.join([word for word in word_tokenize(text) if word not in custom_stopwords])

    for pattern in my_patterns:
        words_without_stopwords = re.sub(pattern, ' ', words_without_stopwords).strip()

    return words_without_stopwords

from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize
import re


def extract_words_without_stopwords(text):

    my_stopwords = ['...', '+44', '\-', '\'s', 'The']

    my_patterns = ['\d{1,4}', '[A-Z]{2,3}', '-', '/']

    custom_stopwords = set(stopwords.words('english') + list(punctuation) + my_stopwords)

    words_without_stopwords = ' '.join([word for word in word_tokenize(text) if word not in custom_stopwords])

    for pattern in my_patterns:
        words_without_stopwords = re.sub(pattern, ' ', words_without_stopwords).strip()

    return words_without_stopwords

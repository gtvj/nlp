from get_text_from_url import get_text_from_url
from get_words_from_text import extract_words_without_stopwords
from ngrams import get_trigrams, get_bigrams
from tokenizer import tokenize_to_words
from summarize_text import get_summary


class DetailsPage():

    def __init__(self, url):

        text = get_text_from_url(
            url,
            element='table',
            attribute='class',
            value='asset-details')

        text_without_stopwords = extract_words_without_stopwords(text)
        tokenized_text = tokenize_to_words(text_without_stopwords)
        self.trigrams = get_trigrams(tokenized_text)
        self.bigrams = get_bigrams(tokenized_text)
        self.summary = get_summary(text, 3)
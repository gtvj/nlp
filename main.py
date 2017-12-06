from get_text_from_url import get_text_from_url
from ngrams import get_bigrams, get_trigrams
from tokenizer import tokenize_to_words
from get_words_from_text import extract_words_without_stopwords

text = get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259',
    element='table',
    attribute='class',
    value='asset-details')

print '----------'
print '---TEXT---'
print '----------'
print text

text_without_stopwords = extract_words_without_stopwords(text)

tokenized_text = tokenize_to_words(text_without_stopwords)

trigrams = get_trigrams(tokenized_text)

print '--------------'
print '---TRIGRAMS---'
print '--------------'
print trigrams

bigrams = get_bigrams(tokenized_text)

print '-------------'
print '---BIGRAMS---'
print '-------------'
print bigrams

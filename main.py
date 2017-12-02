import get_text_from_url
import tokenizer
import remove_stop_words
import find_trigrams
import find_bigrams

text = get_text_from_url.get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259',
    element='table',
    attribute='class',
    value='asset-details')

print '----------'
print '---TEXT---'
print '----------'
print text

text_without_stopwords = remove_stop_words.remove_stopwords(text)

tokenized_text = tokenizer.tokenize_to_words(text_without_stopwords)

trigrams = find_trigrams.get_trigrams(tokenized_text)

print '---------------------------------'
print '---TRIGRAMS INCLUDES STOPWORDS---'
print '---------------------------------'
print trigrams

bigrams = find_bigrams.get_bigrams(tokenized_text)

print '-------------------------------'
print '---BIGRAMS WITHOUT STOPWORDS---'
print '-------------------------------'
print bigrams

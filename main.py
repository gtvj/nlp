import get_text_from_url
import ngrams
import tokenizer
import get_words_from_text
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

text_without_stopwords = get_words_from_text.extract_words_without_stopwords(text)

tokenized_text = tokenizer.tokenize_to_words(text_without_stopwords)

trigrams = ngrams.get_trigrams(tokenized_text)

print '--------------'
print '---TRIGRAMS---'
print '--------------'
print trigrams

bigrams = ngrams.get_bigrams(tokenized_text)

print '-------------'
print '---BIGRAMS---'
print '-------------'
print bigrams

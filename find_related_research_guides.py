import get_text_from_url
import ngrams
import tokenizer
import get_words_from_text
import json

from ngrams import find_ngram_match

text = get_text_from_url.get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259',
    element='table',
    attribute='class',
    value='asset-details')

text_without_stopwords = get_words_from_text.extract_words_without_stopwords(text)
tokenized_text = tokenizer.tokenize_to_words(text_without_stopwords)
trigrams = ngrams.get_trigrams(tokenized_text)
bigrams = ngrams.get_bigrams(tokenized_text)

decorated_guides = json.loads(open('generated/decorated_guides.json', 'r').read())

find_ngram_match(trigrams, decorated_guides, 'trigrams')
find_ngram_match(bigrams, decorated_guides, 'bigrams')

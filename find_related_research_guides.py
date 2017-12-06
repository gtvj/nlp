import json
from get_text_from_url import get_text_from_url
from tokenizer import tokenize_to_words
from ngrams import find_ngram_match, get_bigrams, get_trigrams
from get_words_from_text import extract_words_without_stopwords

text = get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259',
    element='table',
    attribute='class',
    value='asset-details')

text_without_stopwords = extract_words_without_stopwords(text)
tokenized_text = tokenize_to_words(text_without_stopwords)
trigrams = get_trigrams(tokenized_text)
bigrams = get_bigrams(tokenized_text)

decorated_guides = json.loads(open('generated/decorated_guides.json', 'r').read())

find_ngram_match(trigrams, decorated_guides, 'trigrams')
find_ngram_match(bigrams, decorated_guides, 'bigrams')

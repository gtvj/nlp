import get_text_from_url
import tokenizer
import get_words_from_text
import find_trigrams
import find_bigrams
import json

text = get_text_from_url.get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259',
    element='table',
    attribute='class',
    value='asset-details')

text_without_stopwords = get_words_from_text.extract_words_without_stopwords(text)
tokenized_text = tokenizer.tokenize_to_words(text_without_stopwords)
trigrams = find_trigrams.get_trigrams(tokenized_text)
bigrams = find_bigrams.get_bigrams(tokenized_text)

decorated_guides = json.loads(open('generated/decorated_guides.json', 'r').read())

def find_ngram_match(ngram, decorated_guides, type):
    for ngram_in_details in ngram:
        sorted_ngram = sorted(list(ngram_in_details[0]))

        for guide in decorated_guides:
            for item in guide[type]:
                if sorted_ngram in item:
                    print ' '.join(str(e) for e in sorted_ngram) + ' found in ' + guide['guide_href']

find_ngram_match(trigrams, decorated_guides, 'trigrams')
find_ngram_match(bigrams, decorated_guides, 'bigrams')

import json

from details_page import DetailsPage
from ngrams import find_ngram_match
from ngrams import find_reference_match

pages = [
    'http://discovery.nationalarchives.gov.uk/details/r/C543'
]

for page in pages:
    page = DetailsPage(page)

    decorated_guides = json.loads(open('generated/decorated_guides.json', 'r').read())

    print '----------'
    print '---Page---'
    print '----------'

    print page.summary
    print page.trigrams
    print page.bigrams
    print page.references

    print '-----------------------------'
    print '---Guides found by trigram---'
    print '-----------------------------'

    for i in find_ngram_match(page.trigrams, decorated_guides, 'trigrams'):
        print i

    print '-----------------------------'
    print '---Guides found by bigram---'
    print '-----------------------------'
    for i in find_ngram_match(page.bigrams, decorated_guides, 'bigrams'):
        print i

    print '-------------------------------'
    print '---Guides found by reference---'
    print '-------------------------------'

    for i in find_reference_match(page.references, decorated_guides):
        print i

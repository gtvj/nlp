import json

from details_page import DetailsPage
from ngrams import find_ngram_match

page = DetailsPage('http://discovery.nationalarchives.gov.uk/details/r/C259')

decorated_guides = json.loads(open('generated/decorated_guides.json', 'r').read())

print page.summary
find_ngram_match(page.trigrams, decorated_guides, 'trigrams')
find_ngram_match(page.bigrams, decorated_guides, 'bigrams')

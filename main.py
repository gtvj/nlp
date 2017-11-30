import get_text_from_url
import tokenizer

text = get_text_from_url.get_text_from_url(
    'http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-medal-index-cards-1914-1920/')

tokenized_text = tokenizer.tokenize(text)

print tokenized_text
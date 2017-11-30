import get_text_from_url
import tokenizer
import remove_stop_words

text = get_text_from_url.get_text_from_url(
    'http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-medal-index-cards-1914-1920/')

text_without_stopwords = remove_stop_words.remove_stopwords(text)

tokenized_text = tokenizer.tokenize(text_without_stopwords)

print tokenized_text
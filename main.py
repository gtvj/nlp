import get_text_from_url
import tokenizer
import remove_stop_words
import find_bigrams

text = get_text_from_url.get_text_from_url(
    'http://discovery.nationalarchives.gov.uk/details/r/C259')

text_without_stopwords = remove_stop_words.remove_stopwords(text)

tokenized_text = tokenizer.tokenize(text_without_stopwords)

bigrams = find_bigrams.get_bigrams(tokenized_text)

print bigrams
from tokenizer import tokenize_to_sentences, tokenize_to_words
from get_words_from_text import extract_words_without_stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from nltk.tokenize import word_tokenize


def get_summary(text, number_of_sentences_sought):
    sentences = tokenize_to_sentences(text)

    words = ' '.join(tokenize_to_words(text))

    words_without_stopwords = extract_words_without_stopwords(words).split()

    freq = FreqDist(words_without_stopwords)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentences):  # For each sentence
        for w in word_tokenize(sentence.lower()):  # For each word in the sentence
            if w in freq:  # If the word is in freq
                ranking[i] += freq[w]  # add the word frequency to the sentence ranking

    # get the 'n' highest ranked sentences
    sent_ids = nlargest(number_of_sentences_sought, ranking, key=ranking.get)

    return ' '.join([sentences[j] for j in sorted(sent_ids)])

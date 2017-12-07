import re


def extract_references(text):
    matches = re.findall(r"\b[A-Z]{2,5}\s\d{1,5}\b", text)

    cleaned_matches = []

    for match in matches:
        cleaned_matches.append(re.sub('\s', '', match))

    return cleaned_matches

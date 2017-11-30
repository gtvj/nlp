import urllib2
from bs4 import BeautifulSoup
import re

def get_text_from_url(url):
    response = urllib2.urlopen(url)
    response_html = response.read()
    html = BeautifulSoup(response_html, "html.parser")
    clean = clean_html(html)
    just_text = clean.get_text()
    just_text_without_whitespace = remove_extra_whitespace(just_text)
    return just_text_without_whitespace


def remove_styles(html):
    [s.extract() for s in html('style')]
    return html


def remove_scripts(html):
    [s.extract() for s in html('script')]
    return html


def remove_extra_whitespace(text):
    return re.sub('\s+', ' ', text).strip()


def clean_html(html):
    html = remove_scripts(html)
    html = remove_styles(html)
    return html
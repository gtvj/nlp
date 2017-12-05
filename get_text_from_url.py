import urllib2
from bs4 import BeautifulSoup
import re


def get_text_from_url(url, element, attribute, value):
    response = urllib2.urlopen(url)
    response_html = response.read()
    html = BeautifulSoup(response_html, "html.parser").find(element, {attribute: value})
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


def remove_unwanted_elements(html):
    # IDs only, for the time being
    # See https://stackoverflow.com/questions/32063985/deleting-a-div-with-a-particlular-class-using-beautifulsoup
    unwanted_ids = ['breadcrumb', 'breadcrumb-holder']

    for id in unwanted_ids:

        found_el = html.find('div', id=id)

        if found_el:
            found_el.decompose()

    return html


def clean_html(html):
    html = remove_scripts(html)
    html = remove_styles(html)
    html = remove_unwanted_elements(html)
    return html

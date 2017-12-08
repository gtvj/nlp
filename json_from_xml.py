import xml.etree.ElementTree
import pprint
import json
import re

# Improves print formatting
pp = pprint.PrettyPrinter(indent=4)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('matts_data/LettercodeMALLETphrasesBigrams/') if isfile(join('matts_data/LettercodeMALLETphrasesBigrams/', f))]

files = [re.sub('_bigram_phrases.xml', '', f) for f in onlyfiles]

files = ['FO', 'ADM', 'PROB']

output = {}
output['name'] = 'The National Archives'
output['children'] = []

for letter_code in files:

    department = {}
    department['name'] = letter_code
    department['children'] = []
    department['children'].append({'name': 'phrases', 'children': []})

    the_xml = xml.etree.ElementTree.parse(
        'matts_data/LettercodeMALLETphrasesBigrams/' + letter_code + '_bigram_phrases.xml').getroot()

    i = 0
    for topic in the_xml.findall('topic'):

        for child in topic.findall('phrase'):
            phrase = {}
            phrase['name'] = child.text
            phrase['size'] = child.get('count')
            department['children'][i]['children'].append(phrase)

    i += 1

    output['children'].append(department)

json.dump(output, fp=open('generated/departments.json', 'w'), indent=2)

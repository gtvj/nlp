# NLP

## Finding research guides that seem related to a specific details page

Running the `find_related_research_guides.py` module will identify what it thinks might be the guides related to the Discovery details page(s) listed in the script. To do this it:

* creates a 'details page' object which contains:
    1. an NLP generated summary of the details page (See `get_summary()`)
    2. lists of the top bigrams and trigrams (See `get_trigrams()` and `get_bigrams()`)
    3. a list of document references (See `extract_references()`)
* Looks for the top bigrams and trigrams the in the details page to the those found in all research guides (those in the research guides have been pre-compiled by `generate_decorated_research_guides.py` to `/generated/decorated_guides.json`)

### Example 1: Matches found by ngram

For http://discovery.nationalarchives.gov.uk/details/r/C259 it suggests

![Output from find_related_research_guides.py](images/output_from_find_related_research_guides.png)

### Example 2: Matches found by reference

For http://discovery.nationalarchives.gov.uk/details/r/C515 it suggests

![Output from find_related_research_guides.py](images/alt_output_from_find_related_research_guide.png)

## Matt's MALLET data

Matt's MALLET data is contained in the `/matts_data/` directory. This contains a number of sub-directories containing `.txt` files organised by letter code.

The script `json_from_xml.py` is used to extract all MALLET phrase bigrams to a (huge) JSON object in `departments.json`. This can easily be configured to extract specific letter codes by replacing:

```python
files = [re.sub('_bigram_phrases.xml', '', f) for f in onlyfiles]
```

with only the letter code(s) you would like

```python
files = ['AB', 'AE']
```

The resulting JSON object in `departments.json` is then used in the separate [nlp-visualisation](http://www.github.com/gtv/nlp-visualisation) repository to create interactive treemaps
import get_text_from_url
import summarize_text

research_guide_url = 'http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/british-army-medal-index-cards-1914-1920/'

research_guide_text = get_text_from_url.get_text_from_url(research_guide_url, element = 'div', attribute='role', value='main')

print summarize_text.get_summary(research_guide_text, 1)

'''
This will take in the WA State RCW page and extract all the links to the specific regulatory titles. From each of those links, you can reiterate this again to go another layer deeper into any specific title. Once you go enough layers down to where you have raw legal text, you will need a modified script that will exract that for vectorization. I'll modify this into a class later
'''

from bs4 import BeautifulSoup, SoupStrainer
import requests # a reliable way of making requests

soup = requests.get('http://apps.leg.wa.gov/rcw/')

urls = []

for link in BeautifulSoup(soup.content, "html.parser", parse_only=SoupStrainer('a', href=True)):
        urls.append(link['href'])

sublinks = set()

for link in urls:
    if link.startswith('default.aspx?Cite='):
        sublinks.add(link)
        
print sublinks

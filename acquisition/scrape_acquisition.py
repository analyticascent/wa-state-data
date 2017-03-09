'''
This will take in the WA State RCW page and extract all the links to the specific regulatory titles. From each of those links, you can reiterate this again to go another layer deeper into any specific title. Once you go enough layers down to where you have raw legal text, you will need a modified script that will exract that for vectorization. I'll modify this into a class later
'''

from bs4 import BeautifulSoup, SoupStrainer
import requests # a reliable way of making requests

# homepage = raw_input('Enter the regulation homepage: ')

soup = requests.get('http://apps.leg.wa.gov/rcw/')

# default = raw_input('Enter the URL extension for the Titles: ')

default = 'default.aspx?Cite='

urls = []

for link in BeautifulSoup(soup.content, "html.parser", parse_only=SoupStrainer('a', href=True)):
        urls.append(link['href'])

sublinks = []

for link in urls:
    if link.startswith(default):
        sublinks.append(link)

print sublinks
print
print str(len(sublinks)) + " Regulatory Titles"
print

def full_url(sublinks):
    full_urls = []
    for link in sublinks:
        link = 'http://apps.leg.wa.gov/rcw/' + link
        full_urls.append(link)
    return full_urls

print full_url(sublinks)
print
print str(len(full_url(sublinks))) + ' Regulatory Title Links'

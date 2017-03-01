'''
This is the data acquisition script for obtaining text from
Washington state's legal site - http://apps.leg.wa.gov/rcw/

I kind of threw this together as an exploration for what I
happen to be capable of right now. Inspiration is from this
project: http://RegData.org/
'''

# Okay, first off... the libraries

from bs4 import BeautifulSoup # webscraping library
import requests # a reliable way of making requests
import html5lib # a reliable HTML parser


# Now that we have our arsenal, let's zero in our sights

url = "http://apps.leg.wa.gov/rcw/" # All WA state regs!
soup = BeautifulSoup(requests.get(url).text, 'html5lib')

soup = str(soup) # HTML for the homepage stored as string


'''
At this point we now have the HTML for the RCW homepage
stored as a string in 'soup'. So now we need the links
for the specific titles. We now enter phase two...
'''

# Find all instances of 'default.aspx?Cite=' in the HTML.
# We need these to collect more links to scrape later.

sub_urls = [n for n in xrange(len(soup)) if soup.find('default.aspx?Cite=', n) == n]

print len(sub_urls) # You should get 96

def title_urls(sub_urls):
	
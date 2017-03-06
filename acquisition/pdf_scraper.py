'''
A simple script that can be retrofitted to any web domain that
stores PDFs in a sequential link order. Good for when you only
have to increment a number in a series of URLs to get to the
next file you hope to download. 
'''

import urllib2
import time # Not necessary unless you download a lot at once.

# Quickly downloading too many files can get your IP banned.

url = raw_input("Enter invariant part of the web domain: ")

'''
You want to define 'url' as the portion of the domain that
remains unchanged for every file you download, minus the .pdf
extension at the end.
'''

first = raw_input("Enter first number for the PDF link: ")

last = raw_input("Enter last number for the PDF link: ")

for i in range(int(first), int(last)): # Repeat all of below for sequence
    def main():
        download_file(url + str(i) + '.pdf')

'''
To keep my IP from getting banned, I added a three-second
delay to the downloader below (the "time" import).
'''

    def download_file(download_url):
        response = urllib2.urlopen(download_url)
        file = open("pa" + str(i) + ".pdf", 'wb')
        file.write(response.read())
        file.close()
        print("One second...")
        print
        time.sleep(1)
        print("Two seconds...")
        print
        time.sleep(1)
        print("Getting there...")
        print
        time.sleep(1)
        print("Downloaded " + str(i))
        print

    if __name__ == "__main__":
        main()

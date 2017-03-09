# Acquisition Scripts

These are used to acquire the raw text, JSON data, or CSV files that the analysis scripts will process. Mostly webscraping and Socrata API wrappers. 

&nbsp;

### Web Scraping

The primary data source the web scraping script is used for is to acquire the raw text of the [Revised Code of Washington](http://apps.leg.wa.gov/rcw). Each indivial RCW is stored in an array, which is also sorted by what title the RCW falls under. Unless you have a lot of RAM, I do not recomment scraping and storing all the RCW's into a variable at once.

With the scrape_acquisition.py file, all the title links (96 as of this ReadMe) are collected and stored. From there the process can be reiterated with each of those title links to go deeper into subsections until you reach the raw text itself.

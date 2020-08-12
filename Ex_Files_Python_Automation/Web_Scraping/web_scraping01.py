"""
Web Scraping is a popular way to gather data online.
With the amount of data online, it is essential that you learn how to compile
your own data cheaply and efficiently.

3 steps to achieve this objective:
1. Send a Get Query to a web site:
    -> this returns a html based document containing all the web site information
        and thus, setting us up for the next step
2. Parsing:
    -> In this point, we parse the html document making it more navegable and giving away
        for the final step
3. Extract the data we really want.
    -> At this point, we isolate the data we actually need from the web site and store it
        in wherever format we like.
"""

import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

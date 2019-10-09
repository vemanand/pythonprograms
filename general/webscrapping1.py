'''
Demo program showing webscrapping in action
We will scrap data from IMDB topl 250 movies to retrieve movie name, year and rating
'''
from bs4 import BeautifulSoup
import requests
import sys

url = "http://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, features='html.parser')
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
item = 0
for movie in tr:
    item +=1
    title = movie.find('td',{'class':'titleColumn'}).find('a').contents[0]
    year = movie.find('td',{'class':'titleColumn'}).find('span',{'class':'secondaryInfo'}).contents[0]
    rating = movie.find('td',{'class':'ratingColumn imdbRating'}).find('strong').contents[0]
    record = "#item"+str(item)+":"+title + '_' + year + '_'+rating
    print(record)

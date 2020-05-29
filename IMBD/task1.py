import requests,pprint
from bs4 import BeautifulSoup
import json
import pprint
data_list=[]
source=requests.get(' https://www.imdb.com/india/top-rated-indian-movies/').text

soup=BeautifulSoup(source,'lxml')

all_deatils= soup.find('tbody',class_="lister-list")
for lister in all_deatils.find_all('tr'):
	data={}
	name=lister.find('td',class_='titleColumn').a.text
	data['name']=name


	details=lister.find('td',class_='titleColumn').text
	position=details.split()
	data['position']=position[0]

	year=lister.find('span',class_='secondaryInfo').text
	data['year']=year[1:5]



	rating=lister.find('td',class_="ratingColumn imdbRating").strong.text
	data['ratings']=rating


	name=lister.find('td',class_='titleColumn')
	url=name.find('a')['href']
	data['url']='https://www.imdb.com'+url


	data_list.append(data)

pprint.pprint(data_list)

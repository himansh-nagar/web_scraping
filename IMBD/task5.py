import requests,pprint
from bs4 import BeautifulSoup
import json
import pprint
data_list=[]
url_list=[]
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


for k in data_list:
	for u in k:
		if u=='url':
			url_list.append(k[u])



movie_deatils=[]
for url in range(len(url_list)):
	deatils={}
	responce = requests.get(f'{url_list[url]}').text
	soup= BeautifulSoup(responce,'html.parser')

	div1=soup.find('div',class_='title_wrapper').h1.text.split()
	s=' '
	name=div1
	for ss in range(len(name)-1):
		s+=name[ss]+' '
	deatils['name']=s

	div2=soup.find('div',class_='credit_summary_item').text.split('\n')
	director=div2[2:] 
	deatils['directors']=director

	div3=soup.find_all('div',class_='article')

	count = 0
	for i in div3:
		count+=1
		if count == 11:
			text_block = i.find_all("div","txt-block")
			for j in range(len(text_block)): 
				if (j == 0) or (j == 1) or (j==2):
					h4_ = text_block[j].find("h4")
					a_tag = text_block[j]
					if "Country:" in h4_:
						# print(a_tag.text)
						country=a_tag.text.split()
						for c in country:
							if c=='|':
								country.remove('|')
						deatils['Country']=country[1:]
					elif "Language:" in h4_:
						lang=a_tag.text.split()
						for i in lang:
							if i=='|':
								lang.remove('|')
						deatils['Language']=lang[1:]

	div4=soup.find('div',class_='poster').img['src']
	deatils['Image URL']=div4

	div5= soup.find('div',class_='summary_text').text.strip()
	bio=div5
	deatils['Bio']=bio

	div6=soup.find('div',class_='subtext')
	time=div6.time.text.strip()
	deatils['Time']=time
	a_tags=div6.find_all("a")
	list_of_genre=[]
	for t in a_tags:
		list_of_genre.append(t.text)
	deatils['Genre']=list_of_genre[:-1]

	pprint.pprint(deatils)
	movie_deatils.append(deatils)

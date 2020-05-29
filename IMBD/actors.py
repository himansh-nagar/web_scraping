import requests,pprint,time
from bs4 import BeautifulSoup
import json
data_list=[]
source=requests.get(' https://www.imdb.com/india/top-rated-indian-movies/').text
soup=BeautifulSoup(source,'lxml')
all_deatils= soup.find('tbody',class_="lister-list")
for lister in all_deatils.find_all('tr'):
	data={}
	name=lister.find('td',class_='titleColumn').a.text
	data['name']=name
	name=lister.find('td',class_='titleColumn')
	url=name.find('a')['href']
	data['url']='https://www.imdb.com'+url
	data_list.append(data)

all_movie_name=[]
all_movie_cast=[]
# all_movie_cast_details=[]
for movie_name in data_list:
	all_movie_name.append(movie_name['name'])

count=0
for uurl in data_list:
	new_details={}
	needed_url=uurl['url']
	responce=requests.get(f'{needed_url}fullcredits?ref_=tt_cl_sm#cast').text
	soup=BeautifulSoup(responce,'html.parser')
	table=soup.find('table',class_='cast_list')
	tr_tag=table.find_all('tr')
	id_and_name_list=[]
	for i in tr_tag:
		main_dic={}
		a_tag=i.find_all('a')
		for j in a_tag:
			if j.text in a_tag[1]:
				main_dic['name'] =j.text[:-2]
				A_tag=a_tag[1]
				main_dic['imbd ID'] =A_tag['href']
				id_and_name_list.append(main_dic)
	new_details[all_movie_name[count]]= id_and_name_list
	all_movie_cast.append(new_details)
	count+=1
	# all_movie_cast_details.append(all_movie_cast)

pprint.pprint(all_movie_cast)



file=open('all_movie_cast.json','w')
json.dump(all_movie_cast,file)
file.close()





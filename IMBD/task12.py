import requests,pprint,json
from bs4 import BeautifulSoup

responce=requests.get('https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast').text
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
pprint.pprint(id_and_name_list)

file=open('anandcast.json','w')
json.dump(id_and_name_list,file)
file.close()		

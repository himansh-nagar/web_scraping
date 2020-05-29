import requests,json,pprint
from bs4 import BeautifulSoup


responce=requests.get('https://www.imdb.com/title/tt0066763/').text
deatils={}
movie_deatils=[]
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
					# print(lang[1:])
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


file=open('anandmoviedetail.json','w')
json.dump(deatils,file)
file.close()

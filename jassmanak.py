import requests,pprint
from bs4 import BeautifulSoup
import webbrowser
responce = requests.get("https://gaana.com/artist/jass-manak").text
soup=BeautifulSoup(responce,'html.parser')
link_list=[]
main_div=soup.find('div',class_='s_c')
ul=main_div.find_all("ul")
num=2
position=1
for i in range(len(ul)-2):
	UL=ul[num]
	print(position,'.',UL.span.text)
	num+=1
	position+=1
user_song=int(input('\n \n  \t \t  Which SOng Do you want to play '))
link=soup.find_all('div',class_='playlist_thumb_det')
for i in link:
	link_list.append(i.a['href'])
neded_link=link_list[user_song-1]
play=webbrowser.open(neded_link)
print(play)
print('ENJOY THE MUSIC')
import json,pprint
file=open('task5.json','r')
File=json.load(file)
genre_list=[]
for dic in File:
	for key in dic:
		if key=='Genre':
			for g in dic[key]:
				genre_list.append(g)
print(dict( (genre,genre_list.count(genre) ) for genre in genre_list))




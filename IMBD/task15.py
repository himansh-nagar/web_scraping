import json,pprint
file=open('all_movie_cast.json','r')
File=json.load(file)
file.close()
all_name_of_actors=[]
for dic in File:
	for i in dic:
		for dic2 in dic[i]:
			for key2 in dic2:
				if key2=='name':
					all_name_of_actors.append(dic2[key2])

pprint.pprint(dict( (name,all_name_of_actors.count(name) ) for name in set(all_name_of_actors)))

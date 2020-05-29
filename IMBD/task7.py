import json
file=open('task5.json','r')
File=json.load(file)
director_list=[]
for dic in File:
	for key in dic:
		if key=='directors':
			for a in dic[key]:
				director_list.append(a)

print(dict((l,director_list.count(l)) for l in set(director_list)))




############################3#######################

	# for making a file of directors list

################################################



new_file=open('directors.json','w')
json.dump(director_list,new_file)
new_file.close()

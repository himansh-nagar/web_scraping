import json,pprint
# for all deatils of movie
file =open('task5.json','r')
File=json.load(file)
# for all the directors 
D_file =open('directors.json','r')
d_file=json.load(D_file)
main_list=[]
director_and_languae_dic={}
for i in set(d_file):
	lang_list=[]
	for dic in File:
		for key in dic:
			if key=='directors':
				for Dict in dic[key]:
					if Dict==i:
						try:
							for l in dic['Language']:
								lang_list.append(l)
							main_list.append(lang_list)
						except KeyError:
							pass
	language_list=dict( (ld, lang_list.count(ld) ) for ld in set(lang_list))
	director_and_languae_dic[i]=language_list

pprint.pprint(director_and_languae_dic)


new_file=open('director_and_language.json','w')
json.dump(director_and_languae_dic,new_file)
new_file.close()

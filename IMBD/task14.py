import json,pprint
file=open('all_movie_cast.json','r')
File=json.load(file)
file.close()
all_movie_cast=[]
all_movie_cast2=[]
for dic_list in File:
	one_cast_list=[]
	for dic in dic_list:
		cast_list=dic_list[dic]
		one_cast_list.append(cast_list)
	all_movie_cast.append(one_cast_list)

for dic_list_2 in File:
	for dic2 in dic_list_2:
		all_movie_cast2.append(dic_list_2[dic2])


num_list=[]
for i in all_movie_cast:
	num_dic={}
	for first_ele1 in i:
		first_ele=i[first_ele1]
		for dic_list in File:
			for dic in dic_list:
				if first_ele in dic_list[dic]:
					num+=1
			first_ele2=str(first_ele)
			num_dic[first_ele2]=sec_ele2
		num_list.append(num_dic)
		inde+=1
		inde2+=1
	pprint.pprint(num_list)

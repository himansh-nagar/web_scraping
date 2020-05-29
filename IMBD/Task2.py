import json
import pprint
file=open('task1.json','r')
load_file=json.load(file)
year_list=[]
year_list2=[]

for element in load_file:
	for i in element:
		if i=='year' :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
			year_list.append(element[i])

for j in year_list:
	if j not in year_list2:
		year_list2.append(j)

# print(year_list2)

year_dic={}

for year in year_list2:
	new_list=[]
	for dic in load_file:
		for key in dic:
			if key=='year' and dic['year']==year:
				new_list.append(dic)
	year_dic[year]=new_list

pprint.pprint(year_dic)

FILE=open('task2.json','w')
json.dump(year_dic,FILE)
FILE.close()






import json,pprint
file=open('task1.json','r')
File=json.load(file)

year_list=[]
for dic in File:
	for i in dic:
		if i=='year' and dic['year'] not in year_list:
			year_list.append(dic['year'])

year_list.sort()
year_dic={}
for years in year_list:
	years=int(years)-int(years[-1])
	year_dic[years]=[]


for element in File:
	rounded_year=int(element['year'])-int((element['year'])[-1])
	for key in year_dic:
		if rounded_year==key:
			year_dic[key].append(element)

	
pprint.pprint(year_dic)



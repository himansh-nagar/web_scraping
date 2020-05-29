import json
file=open('task5.json','r')
File=json.load(file)
new_list=[]
for dic in File:
	for key in dic:
		if key =='Language':
			for i in dic[key]:
				new_list.append(i)

print (dict( (l, new_list.count(l) ) for l in set(new_list)))






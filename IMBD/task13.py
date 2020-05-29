import json,pprint
moviedettail=open('anandmoviedetail.json','r')
moviedettail_file=json.load(moviedettail)
moviedettail.close()
all_dic={}
movie_cast_file=open('anandcast.json','r')
movie_cast=json.load(movie_cast_file)
all_dic['movie Name']=moviedettail_file
all_dic['cast']=movie_cast
print(all_dic)


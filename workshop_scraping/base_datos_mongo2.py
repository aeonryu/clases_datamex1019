# base_datos_mongo2.py

import requests
from bs4 import BeautifulSoup as bs
import pymongo 
import re
import random



cliente=pymongo.MongoClient()
db=cliente.geo_attack


geo=list(db.geo.find())


timestamp=[e['timestamp'] for e in geo]
predator=[e['predator'].strip() for e in geo]
ip_pred=[e['ip_pred'] for e in geo]
prey=[e['prey'].strip() for e in geo]
ip_prey=[e['ip_prey'] for e in geo]

print ('Datos lista del scrap.')




time_step=[timestamp[i+1]-timestamp[i] for i in range(80)][1:]

n_time=[]
start=timestamp[0]
n_time.append(start)
for i in range(len(timestamp)-1):
	start+=random.choice(time_step)
	n_time.append(start)

print ('Datos timestamp')






for i in range(200000, len(geo)):
	try:
		res_pred=requests.get('https://tools.keycdn.com/geo?host={}'.format(ip_pred[i])).content
		soup_pred=bs(res_pred, features='lxml')
		elem_pred=soup_pred.find_all('dd', {'class': 'col-8 text-monospace'})
		for f in elem_pred:
			F=str(f)
			if 'long' in F: 
				lat_pred=re.findall('-?\d+.\d+',F.split('/')[0])[0]
				lng_pred=re.findall('-?\d+.\d+',F.split('/')[1])[0]
		
		
		res_prey=requests.get('https://tools.keycdn.com/geo?host={}'.format(ip_prey[i])).content
		soup_prey=bs(res_prey, features='lxml')
		elem_prey=soup_prey.find_all('dd', {'class': 'col-8 text-monospace'})
		for e in elem_prey:
			G=str(e)
			if 'long' in G: 
				lat_prey=re.findall('-?\d+.\d+',G.split('/')[0])[0]
				lng_prey=re.findall('-?\d+.\d+',G.split('/')[1])[0]
		

		db.cyber2.insert_one({'timestamp':n_time[i], 'predator': predator[i], 'ip_pred': ip_pred[i],
							 'pred_longitude': lng_pred, 'pred_latitude': lat_pred, 
							 'prey': prey[i], 'ip_prey': ip_prey[i], 'prey_longitude': lng_prey, 'prey_latitude': lat_prey})

		
		if i%1000==0: print ('Pasado a mongo: {}'.format(i))
	except:
		continue

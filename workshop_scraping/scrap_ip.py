# scrap_ip.py


import requests
from bs4 import BeautifulSoup as bs
import pymongo 
import re



client=pymongo.MongoClient()
db=client.geo_attack

geo=list(db.geo.find())



list_ip=[e['ip_pred'] for e in geo]


for i in range(0, len(list_ip), 50):
	
	try:
		res=requests.get('https://tools.keycdn.com/geo?host={}'.format(list_ip[i])).content

		soup=bs(res, features='lxml')

		elem=soup.find_all('dd', {'class': 'col-8 text-monospace'})
		
		#print (res)
		#print (soup)
		#print (elem)
		
		for f in elem:
			F=str(f)
			if 'lat' in F: 
				lat=re.findall('-?\d+.\d+',F.split('/')[0])[0]
				lng=re.findall('-?\d+.\d+',F.split('/')[1])[0]
				
				print (list_ip[i])
				print ({'latitude': lat, 'longitude': lng})
				
	except:
		continue






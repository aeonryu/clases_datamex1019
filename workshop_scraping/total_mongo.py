# total_mongo.py

import pymongo 
import random



cliente=pymongo.MongoClient()
db=cliente.geo_attack

geo=list(db.geo.find())
cyber=list(db.cyber.find())
cyber2=list(db.cyber2.find())


timestamp=[e['timestamp'] for e in geo]
time_step=[timestamp[i+1]-timestamp[i] for i in range(80)][1:]
n_time=[]
start=timestamp[0]
n_time.append(start)
for i in range(len(timestamp)-1):
	start+=random.choice(time_step)
	n_time.append(start)
print ('Datos timestamp')




total=[]
for e in cyber:
	if e['pred_longitude']!=None and e['prey_longitude']!=None:
		total.append(e)



for e in cyber2:
	if len(e['pred_longitude'])!=4 and len(e['prey_longitude'])!=4 and len(e['pred_latitude'])!=4 and len(e['prey_latitude'])!=4:
		total.append(e)





print ((n_time[len(total)]-n_time[0])/60)


lati=[]
longi=[]
for e in total:
	lati.append(e['pred_longitude'])
	lati.append(e['prey_longitude'])
	longi.append(e['pred_latitude'])
	longi.append(e['prey_latitude'])

zippeo=list(zip(longi,lati))

#print (2*len(total)==len(zippeo))




for i in range(len(total)):
	
	try:
	
		db.total_cyber.insert_one({'timestamp':n_time[i], 
								   'predator_longitude': float(total[i]['pred_longitude']), 
								   'predator_latitude': float(total[i]['pred_latitude']),
								   'prey_longitude': float(total[i]['prey_longitude']), 
								   'prey_latitude': float(total[i]['prey_latitude'])})
								  
	except:
		continue




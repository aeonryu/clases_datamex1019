# cyber_attack_threatbutt.py

from selenium import webdriver
from pyvirtualdisplay import Display
import time
import pymongo 


client=pymongo.MongoClient()
db=client.geo_attack


url='https://threatbutt.com/map/'

display=Display(visible=0)
display.start()

driver=webdriver.Firefox()


while 1:
	
	driver.get(url)

	time.sleep(6)

	count=0
	print ('top')
	
	while count<300:

		elemento=driver.find_element_by_id('attackdiv')
		t=elemento.text.split('\n')[-1]

		
		predator=(t.split('('))[0]
		ip_pred=(t.split('('))[1].split(')')[0]
		
		prey=(t.split('('))[1].split(')')[1][-4:]
		ip_prey=(t.split('('))[2].split(')')[0]
		
		print({'timestamp':time.time(), 'predator': predator, 'ip_pred': ip_pred,
		                  'prey': prey, 'ip_prey': ip_prey})
		
		db.geo.insert_one({'timestamp':time.time(), 'predator': predator, 'ip_pred': ip_pred,
		                   'prey': prey, 'ip_prey': ip_prey})
		
		count+=1






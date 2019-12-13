# cyber_attack_threatmap.py


from selenium import webdriver
from pyvirtualdisplay import Display
import time


url='https://threatmap.checkpoint.com/ThreatPortal/livemap.html'


display=Display(visible=0)
display.start()


driver=webdriver.Firefox()
driver.get(url)

time.sleep(3)

cont=0
while cont<10000:
	
	#elemento=driver.find_element_by_id('tableContainer')
	ti=driver.find_element_by_class_name('timeCol')
	a=driver.find_element_by_class_name('attackCol')
	s=driver.find_element_by_class_name('sourceCol')
	ta=driver.find_element_by_class_name('destCol')
	print ({'Time': ti.text, 'Attack': a.text, 'Source': s.text, 'Target': ta.text})

	cont+=1



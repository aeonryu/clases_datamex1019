
'''
import funciones
print (funciones.suma(3,5))
print (funciones.resta(3,5))
print (funciones.multi(3,5))
print (funciones.divi(3,5))
'''



'''
from funciones import suma
print (suma(3,5))
print (resta(3,5))
'''




from funciones import *
#print (suma(3,5))
#print (resta(3,5))
#print (multi(3,5))
#print (divi(3,5))






def total(x):
	a=suma(x,3)
	a=resta(a,9)
	a=multi(a,8)
	return divi(a,2)
	


if __name__=='__main__':
	print (total(7))

	












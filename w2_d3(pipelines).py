
from funciones2 import *



def exe(ruta):
	df=leer(ruta)
	df=clean(df)
	return df


print (exe('data/pokemon.csv'))

print (pd.DataFrame([1,2,3,3,4]))







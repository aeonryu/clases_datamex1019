import pandas as pd


def leer(ruta):
	df=pd.read_csv(ruta)
	return df




def clean(df):
	df=df.drop(columns=['#'])
	df['All_type']=df['Type 1']+df['Type 2']
	return df

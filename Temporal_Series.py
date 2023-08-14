import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters() # PREVINE UM ERRO

dataset = pd.read_csv('./DADOS/AirPassengers.csv')
print(dataset.head())

# VISUALIZANDO O TIPO DE DADOS DOS ATRIBUTOS
print(dataset.dtypes)

# CONVERTENDO A COLUNA "MONTH" PARA O FORMATO DE DATA

dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
dataset = pd.read_csv('./DADOS/AirPassengers.csv', parse_dates= ['Month'], 
                      index_col= 'Month', date_parser= dateparse)
print(dataset.head())

# CRIAÇÃO DA SÉRIE TEMPORAL

ts = dataset['#Passengers']

# VISUALIZANDO UM REGISTRO ESPECÍFICO POR INDICE

print("\nREGISTRO NÚMERO 1:" ,ts[0])

# VISUALIZANDO REGISTRO POR ANO E MES

print('\nMES 5, 1949: ',ts['1949-05'])

# VISUALIZANDO POR DATA ESPECÍFICA

print('\n04/1949: ' ,ts[datetime(1949, 4, 1)])

# VISUALIZANDO INTERVALOS

print('\nDE 1949 ATE 1950:' ,ts['1949-01-01':'1950-12-02'])

# DO COMEÇO ATÉ UMA CERTA DATA

print("\nCINCO PRIMEIROS MESES" ,ts[:'1949-05-01'])

# VISUALIZANDO POR ANO
print("\n1960: ", ts['1960'])

# VALORES MAXIMOS E MINIMOS

# MAXIMO:
print("VALOR MAXIMO: ", ts[ts.index.max()])

# MINIMO:
print('VALOR MINIMO: ', ts[ts.index.min()])

# VISUALIZAÇÃO DA SÉRIE TEMPORAL COMPLETA

plt.plot(ts)
#plt.show()

# VISUALIZANDO GRAFICAMENTE POR ANO

ts_ano = ts.resample('A').sum()
print('\nVISUALIZANDO A SERIE TEMPORAL POR ANO: ',ts_ano)
plt.plot(ts_ano)
#plt.show()

# VISUALIZANDO GRAFICAMENTE POR MES

ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)
#plt.show()

# VISUALIZANDO UM INTERVALO GRAFICAMENTE

ts_inteval = ts['1959-01-01':'1960-12-01']
plt.plot(ts_inteval)
#plt.show()

# DECOMPONDO A SÉRIE TEMPORAL

from statsmodels.tsa.seasonal import seasonal_decompose

decompose = seasonal_decompose(ts)

tendencia = decompose.trend
sazonalidade = decompose.seasonal
aleatorio = decompose.resid

# VISUALIZANDO A SERIE TEMPORAL DECOMPOSTA:

plt.plot(tendencia)
plt.show()

plt.plot(sazonalidade)
plt.show()

plt.plot(aleatorio)
plt.show()
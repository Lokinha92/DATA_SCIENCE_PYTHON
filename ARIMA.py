import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
from datetime import datetime
from pmdarima import auto_arima

dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
dataset = pd.read_csv('./DADOS/AirPassengers.csv', parse_dates= ['Month'], index_col= 'Month', date_parser= dateparse)

# PARAMETRIZANDO O STEPWISE MODEL

modelo = auto_arima(dataset, start_p=1, start_q=1, start_d=0, start_P=0, max_p=6, max_q=6, m=12, 
                    seasonal= True, trace=True, stepwise= True)
print(modelo.aic())

# SEPARANDO OS DADOS DE TREINO E DE TESTE

treino = dataset.loc['1949-01-01':'1959-12-01']
teste = dataset.loc['1960-01-01':]

# TREINANDO O MODELO

modelo.fit(treino)

# PREVENDO O ANO DE 1960 PARA COMPARAR AO TESTE

previsao = modelo.predict(n_periods= 12)
previsao = pd.DataFrame(previsao, index= teste.index, columns= ['#Passengers'])

comparacao = pd.concat([teste, previsao], axis=1).plot()
comparacao

stemporal = pd.concat([dataset, previsao], axis=1).plot(linewidth = 3)
stemporal


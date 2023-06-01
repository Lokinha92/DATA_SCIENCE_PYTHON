import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

dataset = pd.read_csv("DADOS/mt_cars.csv")
dataset = dataset.drop(['Unnamed: 0'], axis= 1)
print(dataset.head())

# CRIAÇÃO DE UM MODELO DE REGRESSÃO LINEAR MULTIPLA PARA PREVER O MPG DE ACORDO COM CYL, DISP E HP

x = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 0].values
print(x)
modelo = LinearRegression()
modelo.fit(x, y)

# prevendo valores através do modelo:

array = np.array([4, 200, 100]) # alterar esses valores para prever com diferentes parametros
array = array.reshape(1, -1)
previsao = modelo.predict(array)
print(previsao)
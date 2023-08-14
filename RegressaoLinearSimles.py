import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

dataset = pd.read_csv("./DADOS/cars.csv")
print(dataset.head())
dataset = dataset.drop(['Unnamed: 0'], axis=1)
print(dataset.head())

# SEPARANDO AS VARIAVEIS ENTRE DEPENDENTES E INDEPENDENTES

x = dataset.iloc[:, 1].values # INDEPENDENTE
y = dataset.iloc[:, 0].values # DEPENDENTE

# CALCULANDO A CORRELAÇÃO:

correlacao = np.corrcoef(x,y)
print("A CORRELAÇÃO É: ", correlacao)

# CRIANDO O MODELO DE REGRESSÃO LINEAR

X = x.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(X,y)

# GERANDO OS GRAFICOS

#Grafico de dispersão dos dados reais:
graficoD = plt.scatter(X,y)
#print(graficoD)

# Grafico contendo a linha de Regressão
PlotRL = plt.plot(X, modelo.predict(X), color= "Red")
#print(PlotRL)

# Grafico de Resíduos

residuo = ResidualsPlot(modelo)
residuo.fit(X,y)
residuo.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

dataset = pd.read_csv("DADOS/slr12.csv", sep= ";")
print(dataset)
print(dataset.shape)

# CRIAÇÃO DO MODELO DE REGRESSAO LINEAR PARA PREVER O CUSTO INICIAL A PARTIR DA TAXA ANUAL

x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values



correlacao = np.corrcoef(x, y)
print("A CORRELAÇÃO É: ",correlacao) # 0.47700725 -> Postiva Fraca

x = x.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(x, y)

plt.scatter(x, y)
grafico = plt.plot(x, modelo.predict(x), color= 'Green')
print(grafico)

#residuais:
#residuo = ResidualsPlot(modelo)
#residuo.fit(x, y)
#residuo.show() # NÃO INDICA PADRÕES E A DISTRIBUIÇÃO SE APROXIMA DA NORMAL. BOM MODELO!

# PREVENDO
prever = float(input("INFORME O VALOR DA TAXA QUE DESEJA PREVER O INVESTIMENTO INICIAL: "))

resultado = modelo.predict([[prever]])

print("O VALOR DO INVESTIMENTO INICIAL (segundo o modelo) PARA A TAXA ", prever, " É: ", resultado)
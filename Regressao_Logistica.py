import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def model(x):
    return 1/(1+np.exp(-x))

dataset = pd.read_csv("DADOS/Eleicao.csv", sep= ";")
print(dataset.head())

plt.scatter(dataset.DESPESAS, dataset.SITUACAO)

correlacao = np.corrcoef(dataset.DESPESAS, dataset.SITUACAO)
print("\nA CORRELAÇÃO É: ", correlacao[0][1]) # -> 0.8121871655764074   FORTE POSITIVA

x = dataset.iloc[:, 2].values
x = x[:, np.newaxis] # -> TRANSFORMANDO O X PARA FORMATO DE MATRIZ
y = dataset.iloc[:, 1].values

modelo = LogisticRegression()
modelo.fit(x, y)

plt.scatter(x, y, color= 'blue')
x_teste = np.linspace(10, 3000, 100)

parametro_PREVISAO = (x_teste * modelo.coef_ + modelo.intercept_)
r = model(parametro_PREVISAO).ravel()
plt.plot(x_teste, r, color= 'red')

# PREVENDO NOVOS DADOS ATRAVÉS DO MODELO

novos_dados = pd.read_csv("DADOS/NovosCandidatos.csv", sep= ";")
print("\nBASE DE NOVOS CANDIDATOS: \n", novos_dados)
dados = novos_dados.iloc[:, 1].values
dados = dados.reshape(-1, 1)

previsao = modelo.predict(dados)
print("PROVAVEIS CANDIDATOS ELEITOS:\n0 = PROVAVELMENTE NAO SE ELEGE, 1 = PROVAVELMENTE ELEITO\n", previsao)

novos_dados = np.column_stack((novos_dados, previsao))
print("AQUI ESTÁ UMA RELAÇÃO ENTRE OS NOVOS CANDIDATOS, SEUS INVESTIMENTOS E A SUA PROVÁVEL SITUAÇÃO ELEITORAL:\n", novos_dados)
import pandas as pd
import numpy as np
dataset = pd.read_csv("./DADOS/iris.csv")

mostra = dataset.head()

shape = dataset.shape

print(mostra)
print(shape)

np.random.seed(2345)

#GERANDO UM ARRAY DE 0 E 1 PARA AMOSTRAGEM SIMPLES
amostra = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.7, 0.3])
tamanho = len(amostra)
print(tamanho)

#MOSTRANDO A QUANTIDADE DE 0 E 1 NO ARRAY ALEATORIO GERADO
tamanho0 = len(amostra[amostra == 0])
tamanho1 = len(amostra[amostra == 1])

print("0 -> ", tamanho0, "\n1-> ", tamanho1)

# SETANDO O BD DE ACORDO COM A AMOSTRA
bd_amostra = dataset.loc[amostra == 0]
print(bd_amostra)
print(bd_amostra.shape)


#%%

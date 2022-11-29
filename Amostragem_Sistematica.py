import pandas as pd
import numpy as np
from math import ceil

# Importando a BD
dataset = pd.read_csv("iris.csv")

#verificando o tamanho da população
print(dataset.shape)

#definindo variáveis representativas
populacao = 150
amostra = 10
k = ceil(populacao/amostra)  # 15 -> vou selecionar um elemento a cada 15

# Definindo de forma aleatória a partir de qual linha vou selecionar os itens
r = np.random.randint(low = 1, high = k+1, size = 1)

# Realizando o sorteio do ID dos itens da amostra
acumulador = r[0]
sorteados = []

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
print(sorteados)

bd_amostra = dataset.loc[sorteados]
print(bd_amostra)

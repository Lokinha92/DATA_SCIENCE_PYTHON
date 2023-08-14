# Algoritmo de tarefa não supervisionada - Agrupador simples que usa a distancia euclidiana para agrupar os dados a partir de um numero de clusters definido pelo usuario
# K-means nao gera ruidos

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()

# visualizando registros unicos por por classe

unicos, quantidade = np.unique(iris.target, return_counts=True)

print(unicos,"\n",quantidade) # Visualização da associação original dos dados

cluster = KMeans(n_clusters= 3) # deve ser o numero de registros unicos de classe, no caso do conjunto de dados, 3.

cluster.fit(iris.data)

centroides = cluster.cluster_centers_ # centroides do processo de agrupamento

agrupamento = cluster.labels_ # o agrupamento feito pelo K-means

unicosKM, quantidadeKM = np.unique(agrupamento, return_counts= True)

print(unicosKM,"\n",quantidadeKM) # visualização dos grupos a qual cada registro foi associado pelo K means

resultados = confusion_matrix(iris.target, agrupamento)

print("\n", resultados)
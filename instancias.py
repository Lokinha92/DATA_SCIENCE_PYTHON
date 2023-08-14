# aprendizado baseado em instancia - não utiliza modelo, usa os dados "em tempo real" para encontrar o elemento mais proximo - conjunto de dados menor

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier #classificador de vizinho mais proximo
from sklearn import datasets
from scipy import stats

#iris = pd.read_csv("./DADOS/iris.csv")
#print(iris.head())

iris = datasets.load_iris()

previsores = iris.data
classe = iris.target

x_treino, x_teste, y_treino, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)

# criando modelo

knn = KNeighborsClassifier(n_neighbors=3) #parametro significa quantos vizinhos mais proximos o classificador vai olhar
knn.fit(x_treino, y_treino)

# previsoes

previsoes = knn.predict(x_teste)

m_confusao = confusion_matrix(y_teste, previsoes)

tx_acerto = accuracy_score(y_teste, previsoes)
print("\n\nA taxa de acerto foi de ", tx_acerto*100, "%")
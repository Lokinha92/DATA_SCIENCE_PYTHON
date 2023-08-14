import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
#import graphviz
from sklearn.tree import export_graphviz

# leitura
credito = pd.read_csv('./DADOS/Credit.csv')
print(credito.head())

#separação dos atributos e da classe
previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:, 20].values

#convertendo itens categoricos
label = LabelEncoder()

previsores[:, 0] = label.fit_transform(previsores[:, 0])
previsores[:, 2] = label.fit_transform(previsores[:, 2])
previsores[:, 3] = label.fit_transform(previsores[:, 3])
previsores[:, 5] = label.fit_transform(previsores[:, 5])
previsores[:, 6] = label.fit_transform(previsores[:, 6])
previsores[:, 8] = label.fit_transform(previsores[:, 8])
previsores[:, 9] = label.fit_transform(previsores[:, 9])
previsores[:, 11] = label.fit_transform(previsores[:, 11])
previsores[:, 13] = label.fit_transform(previsores[:, 13])
previsores[:, 14] = label.fit_transform(previsores[:, 14])
previsores[:, 16] = label.fit_transform(previsores[:, 16])
previsores[:, 18] = label.fit_transform(previsores[:, 18])
previsores[:, 19] = label.fit_transform(previsores[:, 19])

#divisao de dados de treino e teste

X_treino, X_teste, y_treino, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)

# criação e treinamento do modelo

arvore = DecisionTreeClassifier()
arvore.fit(X_treino, y_treino)

#visualização da arvore

export_graphviz(arvore, out_file= "tree.dot")

#previsoes:

previsoes = arvore.predict(X_teste)

print("\n\n", previsoes)

# resultados:

m_confusao = confusion_matrix(y_teste, previsoes) # matriz de confusao
print(m_confusao)

taxa_acerto = accuracy_score(y_teste, previsoes) #tx de acerto
print("\n\nA taxa de acerto é de: ", taxa_acerto*100, "%")

taxa_erro = 1 - taxa_acerto
print("\n\nA taxa de erro é: ", taxa_erro*100, "%")
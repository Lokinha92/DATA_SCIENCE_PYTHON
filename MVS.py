#Máquina de vetor de suporte
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier

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

X_treino, X_teste, y_treino, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=1)

SVM = SVC()

SVM.fit(X_treino, y_treino)

previsoes = SVM.predict(X_teste)
print("\n\n", previsoes)

tx_acerto = accuracy_score(y_teste, previsoes)
print("\n\nA taxa de acerto é: ", tx_acerto*100, "%")

#utilizando o extrTreeClassifier(Random Forest) para extrair as caracteristicas mais importantes

forest = ExtraTreesClassifier()
forest.fit(X_treino, y_treino)

importancias = forest.feature_importances_

print("\n\n", importancias) # verifica a importancia de cada atributo do modelo de treino

# cria um nova base de dados de treino e teste utilizando somente os mais importantes

X_treino2 = X_treino[:, [0,1,2,3]]
X_teste2 = X_teste[:,[0,1,2,3]]

#cria outro modelo usando so os atributos mais relevantes

SVM2 = SVC()
SVM2.fit(X_treino2, y_treino)

previsoes2 = SVM2.predict(X_teste2)

tx_acerto2 = accuracy_score(y_teste, previsoes2)
print("\n\nTx de acerto 2 é de ", tx_acerto2*100, "%")
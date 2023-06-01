#libs
import pandas as pd
from sklearn.model_selection import train_test_split # divide os dados entre treino e teste 
from sklearn.naive_bayes import GaussianNB # NaiveBayes
from sklearn.preprocessing import LabelEncoder #Label Encoder
from sklearn.metrics import confusion_matrix, accuracy_score #matriz de confusao
from yellowbrick.classifier import ConfusionMatrix # matriz de confusao grafica

credito = pd.read_csv('./DADOS/Credit.csv')
print(credito.shape)
print(credito.head())

# separando a classe dos atributos normais

previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20]

#Label Encoder para os atributos categoricos

LE1 = LabelEncoder()
previsores[:,0] = LE1.fit_transform(previsores[:,0])

LE2 = LabelEncoder()
previsores[:,2] = LE2.fit_transform(previsores[:,2])

LE3 = LabelEncoder()
previsores[:,3] = LE3.fit_transform(previsores[:,3])

LE4 = LabelEncoder()
previsores[:,5] = LE4.fit_transform(previsores[:,5])

LE5 = LabelEncoder()
previsores[:,6] = LE5.fit_transform(previsores[:,6])

LE6 = LabelEncoder()
previsores[:,8] = LE6.fit_transform(previsores[:,8])

LE7 = LabelEncoder()
previsores[:,9] = LE7.fit_transform(previsores[:,9])

LE8 = LabelEncoder()
previsores[:,11] = LE8.fit_transform(previsores[:,11])

LE9 = LabelEncoder()
previsores[:,13] = LE9.fit_transform(previsores[:,13])

LE10 = LabelEncoder()
previsores[:,14] = LE10.fit_transform(previsores[:,14])

LE11 = LabelEncoder()
previsores[:,16] = LE11.fit_transform(previsores[:,16])

LE12 = LabelEncoder()
previsores[:,18] = LE12.fit_transform(previsores[:,18])

LE13 = LabelEncoder()
previsores[:,19] = LE13.fit_transform(previsores[:,19])

# Divisao dos dados entre treino e teste

X_treino, X_teste, y_treino, y_teste = train_test_split(previsores, classe, test_size= 0.3, random_state=0)

# Criação e treinamento do modelo

naive_bayes = GaussianNB()
naive_bayes.fit(X_treino, y_treino)

#previsao

previsao = naive_bayes.predict(X_teste)

#geraçao de matriz de confusao e taxa de acerto e erro

mconfusao = confusion_matrix(y_teste, previsao)
print("Matriz de confusao: \n")
print(mconfusao)

taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print("A Taxa de acerto foi de: ",taxa_acerto*100,"%")

# gerando a matriz de confusao visual

v = ConfusionMatrix(GaussianNB())
v.fit(X_treino, y_treino)
v.score(X_teste, y_teste)
v.poof()

# colocando o modelo em produção

novo_credito = pd.read_csv("./DADOS/NovoCredit.csv")

novo_credito = novo_credito.iloc[:,0:20].values

novo_credito[:,0] = LE1.transform(novo_credito[:,0])
novo_credito[:,2] = LE2.transform(novo_credito[:,2])
novo_credito[:,3] = LE3.transform(novo_credito[:,3])
novo_credito[:,5] = LE4.transform(novo_credito[:,5])
novo_credito[:,6] = LE5.transform(novo_credito[:,6])
novo_credito[:,8] = LE6.transform(novo_credito[:,8])
novo_credito[:,9] = LE7.transform(novo_credito[:,9])
novo_credito[:,11] = LE8.transform(novo_credito[:,11])
novo_credito[:,13] = LE9.transform(novo_credito[:,13])
novo_credito[:,14] = LE10.transform(novo_credito[:,14])
novo_credito[:,16] = LE11.transform(novo_credito[:,16])
novo_credito[:,18] = LE12.transform(novo_credito[:,18])
novo_credito[:,19] = LE13.transform(novo_credito[:,19])

previsao_nova = naive_bayes.predict(novo_credito)
print(previsao_nova)
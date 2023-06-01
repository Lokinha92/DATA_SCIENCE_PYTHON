import pandas as pd
from sklearn.model_selection import train_test_split

# AMOSTRAGEM ESTRATIFICADA COM ATRIBUTOS BALANCEADOS

dataset = pd.read_csv("./DADOS/iris.csv")
mostra = dataset.head()
print(mostra)

# Verificando se os atributos estão balanceados

classes = dataset['class'].value_counts()
print(classes)

# Realizando a amostra

previsores = dataset.iloc[:, 1:4]
dependente = dataset.iloc[:, 4]

x, _, y, _ = train_test_split(previsores, dependente, test_size=0.5, stratify=dependente)
amostra = y.value_counts()
print(amostra)
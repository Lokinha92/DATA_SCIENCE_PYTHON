import pandas as pd
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("./DADOS/infert.csv")
mostra = dataset.head()
print(mostra)

# Verificando o balanceamento dos dados
escolaridade = dataset['education'].value_counts()
print(escolaridade)

# Realizando a amostra pegando 40% de cada valor
previsor = dataset.iloc[:, 2:9]
dependente = dataset.iloc[:, 1]

x, _, y, _ = train_test_split(previsor, dependente, test_size=0.6, stratify=dependente)
amostra = y.value_counts()

print(amostra)

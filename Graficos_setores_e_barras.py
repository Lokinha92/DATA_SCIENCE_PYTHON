import pandas as pd

dataset = pd.read_csv("insect.csv")

mostra = dataset.head()
print(mostra)

agrupado = dataset.groupby(['spray'])['count'].sum()

#Grafico de barras:

#agrupado.plot.bar(color = "green")

#Grafico de pizza/setores:

agrupado.plot.pie()
import pandas as pd
import seaborn as sns


dataset = pd.read_csv('./DADOS/trees.csv')

shape = dataset.shape

print(shape)

dados = dataset.head()
print(dados,'\n\n')

#histograma = sns.distplot(dataset.iloc[:,1], hist = True, kde = False, bins = 6, color = 'blue', hist_kws={'edgecolor': 'black'})

#linha_dens = sns.distplot(dataset.iloc[:,1], hist = False, kde = True, bins = 6, color = 'blue', hist_kws={'edgecolor': 'black'})

histodens = sns.distplot(dataset.iloc[:,1], hist = True, kde = True, bins = 6, color = 'blue', hist_kws={'edgecolor': 'black'})

#print(histograma)
#print(linha_dens)
print(histodens)
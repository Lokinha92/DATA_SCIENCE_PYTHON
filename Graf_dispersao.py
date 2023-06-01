import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv('./DADOS/trees.csv')

shape = dataset.shape

print(shape)

dados = dataset.head()
print(dados,'\n\n')

disp_pontos = plt.scatter(dataset.Girth, dataset.Volume, color = 'green', facecolors = 'none', marker = '.')
#disp_linhas = plt.plot(dataset.Girth, dataset.Volume)
plt.title('Arvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')

print(disp_pontos) #2.1 caderno
#print(disp_linhas)  #2.2 caderno

disp_pontos_seaborn = sns.regplot(dataset.Girth, dataset.Volume, data = dataset, x_jitter = 0.3, fit_reg=False)
print(disp_pontos_seaborn)

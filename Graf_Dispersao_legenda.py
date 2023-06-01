import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./DADOS/co2.csv')

mostra = dataset.head()

print(mostra)

x = dataset.conc
y = dataset.uptake

unicos = list(set(dataset.Treatment))
print(unicos)

for i in range(len(unicos)):
    index = dataset.Treatment == unicos[i]
    plt.scatter(x[index], y[index], label = unicos[i])
    
plt.legend(loc = 'lower right')
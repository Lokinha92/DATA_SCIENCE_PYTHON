import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("./DADOS/trees.csv")
mostra = dataset.head()

print(mostra)

#plt.boxplot(dataset.Volume, vert = False, showfliers= True, notch = True, patch_artist= True)
#plt.title("Arvores")
#plt.xlabel("Volume")

plt.boxplot(dataset)
plt.title("Arvores")
plt.xlabel("Dados")